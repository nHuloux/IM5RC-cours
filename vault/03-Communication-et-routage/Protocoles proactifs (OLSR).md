---
title: "Protocoles proactifs (OLSR)"
chapitre: 3 - La communication dans les réseaux de capteurs
type: protocole
tags: [reseaux-de-capteurs, chapitre-3, protocole]
---

# Protocoles proactifs (OLSR)

> **Définition.** Protocoles table-driven qui maintiennent en permanence, dans chaque nœud, une table de routage à jour vers toutes les destinations possibles.

**Avantage** : la route est immédiatement disponible, latence minimale. **Inconvénient** : le maintien permanent des tables consomme bande passante et énergie même sans trafic — peu efficace si les communications sont rares. **Exemple : OLSR** (Optimized Link State Routing), qui optimise la diffusion des messages de contrôle grâce aux relais multipoints (MPR).

## Comment choisir entre proactif et réactif

| Situation | Famille adaptée | Pourquoi |
|---|---|---|
| Trafic dense et continu | proactif | les tables entretenues sont amorties par l'usage |
| Trafic sporadique, quelques messages par heure | réactif | rien ne circule quand rien n'a besoin de circuler |
| Topologie stable (nœuds fixes) | proactif, ou RPL | les routes calculées restent valables longtemps |
| Topologie mobile (drones, véhicules) | réactif | les tables proactives seraient périmées avant d'être utiles |
| Trafic essentiellement montant vers une passerelle | **RPL** | l'arbre de collecte est la structure exacte du besoin |
| Latence critique sur un voisinage restreint | hybride (ZRP) | proactif localement, réactif au loin |

**À retenir.** Le critère n'est pas « quel protocole est le meilleur » mais le rapport entre le coût du trafic de contrôle et le volume de trafic utile. Pour les WSN, où le trafic est rare et monte vers un unique point, ce raisonnement conduit presque toujours à [[RPL]].

## Références

- RFC 3626 — OLSR. Révisé par la RFC 7181 (OLSRv2).

## Notions liées

- [[Routage dans les réseaux ad-hoc]]
- [[Protocoles réactifs (AODV)]]
- [[Protocoles hybrides (ZRP)]]
- [[RPL]]

---
*Chapitre 3 — La communication dans les réseaux de capteurs. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
