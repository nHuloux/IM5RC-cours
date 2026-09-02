---
title: "Structure d'une adresse IPv6"
chapitre: 2 - Adressage et protocole IPv6
type: concept
tags: [reseaux-de-capteurs, chapitre-2, concept]
---

# Structure d'une adresse IPv6

> **Définition.** Adresse de 128 bits écrite en hexadécimal, huit groupes de 16 bits séparés par ':', décomposée en préfixe réseau (64 bits) et identifiant d'interface (64 bits).

Deux règles de simplification allègent l'écriture : on peut omettre les zéros de tête de chaque groupe, et remplacer une seule suite de groupes nuls consécutifs par `::` (une seule fois par adresse). Exemple : `2001:0db8:0000:0000:0000:ff00:0042:8329` se réduit à `2001:db8::ff00:42:8329`.

Les 64 bits de poids fort forment le **préfixe réseau** (noté en CIDR, ex. `/64`), qui identifie le sous-réseau. Les 64 bits de poids faible forment l'**identifiant d'interface**, qui identifie l'hôte. Il peut être dérivé de l'adresse MAC par le procédé **EUI-64**, ou tiré aléatoirement pour des raisons de vie privée.

## Repères chiffrés

Découpage courant des 128 bits :

| Champ | Longueur | Rôle |
|---|---|---|
| Préfixe global | 48 bits | délégué par l'opérateur ou le RIR |
| Identifiant de sous-réseau | 16 bits | découpage interne, jusqu'à 65 536 sous-réseaux |
| Identifiant d'interface | 64 bits | identifie le nœud sur le lien |

**Le procédé EUI-64**, à savoir appliquer. À partir d'une adresse MAC de 48 bits :
1. Couper la MAC en deux moitiés de 24 bits.
2. Insérer `FFFE` entre les deux.
3. Inverser le 7ᵉ bit du premier octet (bit U/L, *Universal/Local*).

Exemple : MAC `00:1A:2B:3C:4D:5E` donne l'identifiant `021A:2BFF:FE3C:4D5E`, et donc l'adresse link-local `fe80::21a:2bff:fe3c:4d5e`.

**Point de vigilance pour les capteurs.** Un identifiant dérivé de l'EUI-64 est déductible du contexte, donc élidable par la compression IPHC de [[6LoWPAN]] : c'est ce qui permet de descendre l'en-tête IPv6 à 2 octets sur le lien local. Un identifiant tiré aléatoirement protège mieux la vie privée mais coûte des octets dans chaque trame. Le compromis vie privée / énergie est ici direct.

## Notions liées

- [[IPv6]]
- [[SLAAC]]
- [[6LoWPAN]]
- [[Types d'adresses IPv6]]

---
*Chapitre 2 — Adressage et protocole IPv6. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
