---
title: "Types d'adresses IPv6"
chapitre: 2 - Adressage et protocole IPv6
type: concept
tags: [reseaux-de-capteurs, chapitre-2, concept]
---

# Types d'adresses IPv6

> **Définition.** IPv6 abandonne le broadcast d'IPv4 au profit de trois modes : unicast, multicast et anycast.

- **Unicast** : identifie une interface unique. On distingue les adresses *link-local* (préfixe `fe80::/10`, valables uniquement sur le lien local, auto-configurées systématiquement) et les adresses *globales* (routables sur Internet, préfixe `2000::/3`).
- **Multicast** : identifie un groupe d'interfaces (préfixe `ff00::/8`) ; le paquet est livré à tous les membres. IPv6 s'appuie fortement sur le multicast, notamment pour la découverte de voisins.
- **Anycast** : identifie un groupe d'interfaces, mais le paquet n'est livré qu'au membre le plus « proche » au sens du routage.

**À retenir.** Il n'y a pas de broadcast en IPv6 : il est remplacé par le multicast, plus économe car seuls les nœuds concernés traitent le paquet. Point important pour les réseaux de capteurs, où réveiller inutilement tous les nœuds gaspillerait de l'énergie.

## Notions liées

- [[IPv6]]
- [[NDP (Neighbor Discovery Protocol)]]

---
*Chapitre 2 — Adressage et protocole IPv6. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
