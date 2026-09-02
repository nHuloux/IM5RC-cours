#!/usr/bin/env python3
"""
Génère index.html à partir du dossier vault/.

    python3 build.py

Lit chaque .md de vault/, en extrait le front-matter, le corps et les liens
[[...]], puis injecte le tout dans template.html entre les marqueurs
/*__DATA__*/ et /*__ENDDATA__*/. Le site produit est un fichier unique, sans
dépendance locale : il suffit de le servir tel quel (GitHub Pages, ou
`python3 -m http.server` en local).

Aucune dépendance externe.
"""
import json
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parent
VAULT = ROOT / "vault"
TEMPLATE = ROOT / "template.html"
OUTPUT = ROOT / "index.html"

# Notes non publiées (README interne, changelog, etc.)
SKIP = {"README", "CHANGELOG"}

FM_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.S)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]+)?\]\]")
CODEBLOCK_RE = re.compile(r"```.*?```", re.S)
INLINECODE_RE = re.compile(r"`[^`\n]*`")


def nfc(s: str) -> str:
    return unicodedata.normalize("NFC", s)


def parse_front_matter(text: str):
    """Retourne (dict, corps). Parseur volontairement minimal : clé: valeur."""
    m = FM_RE.match(text)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key, value = key.strip(), value.strip()
        if value.startswith("[") and value.endswith("]"):
            meta[key] = [v.strip() for v in value[1:-1].split(",") if v.strip()]
        else:
            meta[key] = value.strip().strip('"').strip("'")
    return meta, text[m.end():]


def excerpt(body: str) -> str:
    """Première phrase de la définition, pour la colonne de la vue liste."""
    for line in body.splitlines():
        line = line.strip()
        if line.startswith(">"):
            line = re.sub(r"^>\s*", "", line)
            line = re.sub(r"\*\*D[ée]finition\.\*\*\s*", "", line)
            line = re.sub(r"\[\[([^\]|#]+)(?:\|([^\]]+))?\]\]", lambda m: m.group(2) or m.group(1), line)
            line = re.sub(r"[*`_]", "", line)
            return line[:180]
    for line in body.splitlines():
        line = line.strip()
        if line and not line.startswith("#") and not line.startswith("---"):
            line = re.sub(r"[*`_]", "", line)
            return line[:180]
    return ""


def extract_links(body: str):
    """Liens [[...]] hors blocs de code."""
    clean = CODEBLOCK_RE.sub("", body)
    clean = INLINECODE_RE.sub("", clean)
    out, seen = [], set()
    for target in WIKILINK_RE.findall(clean):
        t = nfc(target.strip())
        if t and t not in seen:
            seen.add(t)
            out.append(t)
    return out


def collect():
    if not VAULT.is_dir():
        sys.exit(f"Dossier introuvable : {VAULT}")
    notes = []
    for path in sorted(VAULT.rglob("*.md")):
        stem = nfc(path.stem)
        if stem in SKIP or stem.startswith("CHANGELOG"):
            continue
        raw = path.read_text(encoding="utf-8")
        meta, body = parse_front_matter(raw)
        rel = path.relative_to(VAULT).parent.as_posix()
        notes.append({
            "title": nfc(meta.get("title") or stem),
            "folder": "" if rel == "." else rel,
            "type": meta.get("type", ""),
            "chapter": meta.get("chapitre", ""),
            "tags": meta.get("tags", []) if isinstance(meta.get("tags"), list) else [],
            "body": body.strip("\n"),
            "excerpt": excerpt(body),
            "links": extract_links(body),
        })
    return notes


def report(notes):
    titles = {n["title"] for n in notes}
    dead = {}
    for n in notes:
        for link in n["links"]:
            if link not in titles:
                dead.setdefault(link, []).append(n["title"])
    edges = set()
    for n in notes:
        for link in n["links"]:
            if link in titles and link != n["title"]:
                edges.add(tuple(sorted((n["title"], link))))
    print(f"  {len(notes)} notions, {len(edges)} liens uniques")
    if dead:
        print("  ATTENTION, liens morts :")
        for target, sources in sorted(dead.items()):
            print(f"    [[{target}]] cité par {', '.join(sources)}")
    else:
        print("  aucun lien mort")


def main():
    notes = collect()
    report(notes)
    payload = json.dumps({"notes": notes}, ensure_ascii=False, separators=(",", ":"))
    # neutralise toute séquence qui fermerait la balise <script>
    payload = payload.replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")

    template = TEMPLATE.read_text(encoding="utf-8")
    start, end = "/*__DATA__*/", "/*__ENDDATA__*/"
    i, j = template.find(start), template.find(end)
    if i < 0 or j < 0:
        sys.exit("Marqueurs /*__DATA__*/ … /*__ENDDATA__*/ absents de template.html")
    html = template[: i + len(start)] + payload + template[j:]
    OUTPUT.write_text(html, encoding="utf-8")
    print(f"  écrit {OUTPUT.relative_to(ROOT)} ({len(html) / 1024:.0f} ko)")


if __name__ == "__main__":
    main()
