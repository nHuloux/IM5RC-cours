---
title: "Agrégation de données"
chapitre: 4 - Économie d'énergie et tolérance aux pannes
type: concept
tags: [reseaux-de-capteurs, chapitre-4, concept]
---

# Agrégation de données

> **Définition.** Plutôt que de faire remonter chaque mesure brute, un nœud (ou un chef de cluster) combine les mesures de plusieurs sources en une valeur synthétique et ne transmet que celle-ci.

C'est l'un des grands intérêts de la topologie hiérarchique. Second levier voisin : la **compression et le filtrage local**, qui consiste à ne transmettre que ce qui change (transmission événementielle plutôt que périodique) ou à compresser les données avant envoi. On peut aussi économiser en ajustant la puissance d'émission au strict nécessaire, et en choisissant des routes économes en énergie qui ménagent les nœuds à faible batterie plutôt que le plus court chemin.

**Exemple.** Dans un vignoble, plutôt que d'envoyer chaque minute la mesure de 20 capteurs d'humidité d'une même parcelle, le chef de cluster peut n'envoyer que la moyenne et l'écart-type par quart d'heure, plus une alerte immédiate si un capteur passe sous un seuil critique. Le volume transmis — et donc l'énergie — est divisé par un facteur important, sans perte d'information utile à la décision.

**À retenir.** Trois leviers d'économie à connaître : duty cycling (éteindre la radio au maximum), agrégation (calculer localement pour transmettre moins) et energy harvesting (recharger depuis l'environnement). Le premier est le plus universel et le plus puissant.

## Notions liées

- [[Topologie hiérarchique (clusters)]]
- [[Unité de traitement]]
- [[Duty cycling]]
- [[Mécanismes de résilience]]

---
*Chapitre 4 — Économie d'énergie et tolérance aux pannes. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
