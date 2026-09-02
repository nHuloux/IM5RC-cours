---
title: "Contraintes des réseaux de capteurs"
chapitre: 1 - Introduction, architectures et applications
type: concept
tags: [reseaux-de-capteurs, chapitre-1, concept]
---

# Contraintes des réseaux de capteurs

> **Définition.** Ce qui distingue un WSN d'un réseau informatique classique : énergie limitée, ressources de calcul/mémoire réduites, bande passante faible, environnement hostile, passage à l'échelle, coût.

- **Énergie limitée** : nœuds alimentés par pile, souvent en lieux difficiles d'accès. L'énergie est *la* ressource critique.
- **Ressources de calcul et de mémoire réduites** : quelques dizaines à quelques centaines de kilo-octets de mémoire, microcontrôleur à quelques MHz. Les protocoles doivent être légers.
- **Bande passante faible** : de quelques centaines de bits/s (LoRa) à quelques centaines de kbit/s (Zigbee).
- **Environnement de déploiement hostile** : extérieur, intempéries, interférences, lien radio intrinsèquement peu fiable.
- **Passage à l'échelle et auto-organisation** : un réseau peut compter des milliers de nœuds qu'on ne peut configurer un par un.
- **Contrainte de coût** : le nœud doit être bon marché pour être déployé en grand nombre, ce qui limite la qualité des composants.

Comprendre ces contraintes, c'est comprendre pourquoi tous les protocoles étudiés dans le cours (6LoWPAN, routage ad-hoc, RPL...) sont conçus comme ils le sont.

## Notions liées

- [[Réseau de capteurs sans fil (WSN)]]
- [[Unité d'alimentation]]
- [[6LoWPAN]]
- [[Duty cycling]]
- [[Budget énergétique d'un nœud]]

---
*Chapitre 1 — Introduction, architectures et applications. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
