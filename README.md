# Réseaux de capteurs [IM5RC] — graphe de notions

Version web du vault Obsidian du cours *Réseaux de capteurs* (MIRA, 3ᵉ année) :
57 notions liées entre elles, avec une **vue note**, une **vue graphe** et une
**vue liste**, dans une interface qui reprend celle d'Obsidian.

Le site est un **fichier statique unique** (`index.html`, ~190 ko). Aucun
serveur, aucun build Node, aucune dépendance à installer.

---

## Mettre en ligne sur GitHub Pages

1. Créer un dépôt (public ou privé avec Pages activé), par exemple `im5rc-graphe`.
2. Y pousser le contenu de ce dossier :

   ```bash
   git init
   git add .
   git commit -m "Graphe de notions IM5RC"
   git branch -M main
   git remote add origin git@github.com:<compte>/im5rc-graphe.git
   git push -u origin main
   ```

3. Sur GitHub : **Settings → Pages**, section *Build and deployment* →
   **Source : Deploy from a branch**, **Branch : `main` / `/ (root)`**, puis *Save*.
4. Au bout d'une minute, le site est servi sur
   `https://<compte>.github.io/im5rc-graphe/`.

Rien d'autre à configurer : `index.html` est déjà généré et committé, et le
fichier `.nojekyll` désactive le traitement Jekyll.

### Tester en local avant de pousser

```bash
python3 -m http.server 8000
# puis ouvrir http://localhost:8000
```

(Ouvrir `index.html` par double-clic fonctionne aussi, mais servir en HTTP est
plus fidèle au comportement de GitHub Pages.)

---

## Mettre à jour le contenu

Les notes sont dans `vault/`, exactement dans le format du vault Obsidian.
Après toute modification :

```bash
python3 build.py
```

Le script relit tous les `.md` de `vault/`, en extrait le front-matter, le corps
et les liens `[[…]]`, et réinjecte les données dans `index.html`. Il affiche au
passage le nombre de notions, le nombre de liens, et **la liste des liens
morts** s'il y en a — pratique pour repérer une note renommée.

```
$ python3 build.py
  57 notions, 265 liens uniques
  aucun lien mort
  écrit index.html (188 ko)
```

Le même dossier `vault/` peut être ouvert directement dans Obsidian
(*Open folder as vault*) : le site et l'application locale partagent la source.

---

## Ce que fait l'interface

| | |
|---|---|
| **Vue note** | rendu markdown complet : wikilinks cliquables, tableaux, schémas Mermaid rendus, citations de définition mises en valeur |
| **Vue graphe** | simulation de forces sur canvas, couleur par chapitre, taille par nombre de liens. Molette = zoom, glisser le fond = déplacer, glisser un nœud = le repositionner, clic = ouvrir la note. Filtres par chapitre, curseurs d'écartement et de densité d'étiquettes |
| **Vue liste** | tableau triable de toutes les notions (titre, chapitre, type, nombre de liens) avec l'amorce de chaque définition, filtrable par chapitre |
| **Panneau gauche** | explorateur de fichiers par dossier, recherche plein texte (titre **et** corps) |
| **Panneau droit** | graphe local de la note, liens sortants, liens entrants (backlinks), plan de la note |

Raccourcis : `⌘K` / `Ctrl+K` pour la recherche, `n` / `g` / `l` pour changer de
vue, `Échap` pour vider la recherche. Les flèches de la barre d'outils
rejouent l'historique de navigation.

Le thème suit celui du système et se bascule avec l'icône en bas de la barre
latérale ; le choix est mémorisé dans le navigateur.

Chaque note a son URL : `…/#/n/RPL`, `…/#/n/6LoWPAN`. Les liens sont donc
partageables et l'historique du navigateur fonctionne.

---

## Structure du dépôt

```
index.html      le site, généré — c'est le seul fichier servi
template.html   le gabarit (HTML + CSS + JS) sans les données
build.py        vault/*.md  →  index.html
vault/          les 57 notes markdown, format Obsidian
.nojekyll       désactive Jekyll sur GitHub Pages
```

Ne pas éditer `index.html` à la main : il est écrasé à chaque `build.py`. Les
modifications de contenu vont dans `vault/`, celles d'interface dans
`template.html`.

---

## Dépendances externes

Deux bibliothèques sont chargées depuis cdnjs, version épinglée :

- [marked](https://marked.js.org) 12.0.2 — rendu markdown
- [mermaid](https://mermaid.js.org) 10.9.1 — rendu des schémas

Les polices viennent de Google Fonts (Figtree, Source Serif 4, JetBrains Mono),
avec des polices système en repli. Le reste — moteur de graphe, recherche,
routage — est écrit à la main dans `template.html`, sans framework.

Pour un site totalement autonome (intranet sans accès Internet), télécharger
`marked.min.js` et `mermaid.min.js` dans un dossier `vendor/`, puis remplacer
les deux URL cdnjs dans `template.html` avant de relancer `build.py`. Sans ces
deux bibliothèques, la navigation et le graphe continuent de fonctionner, mais
les notes s'affichent en markdown brut.

---

*Généré à partir du support `26-27_COURS_IPG_INGE_Reseaux-capteurs-IM5RC-Support-complet.tex`.
Les schémas et les notions du dossier `vault/05-Complements/` ont été ajoutés
directement dans le vault et ne figurent pas encore dans le `.tex`.*
