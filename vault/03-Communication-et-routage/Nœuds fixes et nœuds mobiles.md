---
title: "Nœuds fixes et nœuds mobiles"
chapitre: 3 - La communication dans les réseaux de capteurs
type: concept
tags: [reseaux-de-capteurs, chapitre-3, concept]
---

# Nœuds fixes et nœuds mobiles

> **Définition.** Un nœud fixe, posé une fois, donne une topologie stable ; un nœud mobile rend la topologie dynamique et le routage difficile.

Dans la majorité des déploiements (agriculture, bâtiment, surveillance), les nœuds sont **fixes** : les routes changent peu, la principale cause de changement est la défaillance d'un nœud, pas son déplacement.

Certains nœuds se **déplacent** (animaux, véhicules, personnes, drones) : la topologie devient dynamique, les voisins changent en permanence, les routes se rompent et doivent être reconstruites sans cesse — ce qui coûte des messages de contrôle et de l'énergie.

On distingue aussi la **mobilité de la passerelle** : un collecteur mobile (véhicule, drone) qui parcourt la zone pour récolter les données des nœuds fixes au passage (*data mule*), économisant l'énergie des nœuds au prix d'une latence de collecte plus élevée.

**À retenir.** Nœuds fixes ⇒ topologie stable, routes durables, optimisation possible. Nœuds mobiles ⇒ topologie changeante, routes à reconstruire fréquemment, protocoles réactifs indispensables. La mobilité est le facteur qui rend le routage difficile.

## Notions liées

- [[Nœud capteur (mote)]]
- [[Réseau ad-hoc (MANET)]]
- [[Protocoles réactifs (AODV)]]
- [[RPL]]

## Mentionné par

- [[NB-IoT et LTE-M]]

---
*Chapitre 3 — La communication dans les réseaux de capteurs. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
