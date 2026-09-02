---
title: "Tolérance aux pannes"
chapitre: 4 - Économie d'énergie et tolérance aux pannes
type: concept
tags: [reseaux-de-capteurs, chapitre-4, concept]
---

# Tolérance aux pannes

> **Définition.** Capacité d'un réseau à continuer de fournir son service, éventuellement en mode dégradé, en dépit de la défaillance d'une partie de ses composants (nœuds, liens, passerelle).

Dans un WSN, la panne n'est pas l'exception mais la **règle statistique** : avec des centaines de nœuds bon marché, déployés en environnement hostile, il est certain qu'à tout instant certains seront hors service (batterie épuisée, destruction physique, défaillance matérielle, perte temporaire du lien radio). La tolérance aux pannes n'est pas gratuite : la redondance augmente le nombre de nœuds (coût) et le trafic de surveillance (énergie) — l'ingénieur doit doser le niveau de résilience selon la **criticité** de l'application.

**Exemple.** Vignoble : la perte ponctuelle de quelques capteurs d'humidité n'est pas grave (on interpole) — redondance légère suffisante. Prévention incendie : application critique, un trou de couverture peut laisser passer un départ de feu — forte redondance, chemins multiples, passerelle de secours indispensables. Site industriel : la maintenance prédictive tolère une perte temporaire, mais une alarme de sécurité doit être garantie.

**À retenir.** Dans un WSN, on conçoit pour la panne, pas contre elle. Les parades : redondance (des nœuds, des chemins, de la passerelle) et auto-guérison (détection + reconfiguration automatique). Le bon niveau de tolérance se règle sur la criticité de l'application et se paie en coût et en énergie.

## Notions liées

- [[Mécanismes de résilience]]
- [[Topologie maillée (mesh)]]

---
*Chapitre 4 — Économie d'énergie et tolérance aux pannes. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
