---
title: "Chapitre 4 - Économie d'énergie et tolérance aux pannes"
type: moc
tags: [reseaux-de-capteurs, moc, chapitre-4]
---

# Chapitre 4 - Économie d'énergie et tolérance aux pannes

Notions du chapitre 4 — *Économie d'énergie et tolérance aux pannes*.

- [[Budget énergétique d'un nœud]] — Estimation de l'autonomie d'un nœud à partir de la capacité de sa source d'énergie et de sa consommation moyenne : T_vie ≈ C / I_moy.
- [[Duty cycling]] — Fait alterner le nœud entre un état actif (radio et capteurs allumés) et un état de sommeil profond, en maximisant le temps de sommeil. Le rapport cyclique (duty cycle) est la fraction de temps passée en état actif.
- [[Agrégation de données]] — Plutôt que de faire remonter chaque mesure brute, un nœud (ou un chef de cluster) combine les mesures de plusieurs sources en une valeur synthétique et ne transmet que celle-ci.
- [[Récupération d'énergie (energy harvesting)]] — Capter de l'énergie dans l'environnement du nœud pour recharger sa réserve : solaire, cinétique, thermique, ou radiofréquence.
- [[Tolérance aux pannes]] — Capacité d'un réseau à continuer de fournir son service, éventuellement en mode dégradé, en dépit de la défaillance d'une partie de ses composants (nœuds, liens, passerelle).
- [[Mécanismes de résilience]] — Ensemble des parades qui permettent à un WSN d'encaisser la perte de composants : redondance spatiale, redondance des chemins, auto-guérison, redondance de la passerelle, agrégation résiliente.

## Compléments rattachés à ce chapitre

- [[Le fil rouge de l'énergie]] — note transversale : tous les endroits où le cours revient sur son principe directeur.
- [[Couche MAC et accès au canal (CSMA-CA)]] — pourquoi faire dormir un nœud n'est pas gratuit.
- [[TSCH]] — rendre le rapport cyclique déterministe.
- [[LEACH]] — faire tourner un rôle coûteux en énergie plutôt que mieux le choisir.
- [[Sécurité des réseaux de capteurs]] — le *denial of sleep*, attaque qui vise directement le budget énergétique.

## Voir aussi

- [[Accueil]]
- [[Chapitre 1 - Introduction, architectures et applications]]
- [[Chapitre 2 - Adressage et protocole IPv6]]
- [[Chapitre 3 - La communication dans les réseaux de capteurs]]
- [[Compléments hors support]]
