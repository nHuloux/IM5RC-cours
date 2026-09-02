---
title: "Le fil rouge de l'énergie"
chapitre: Compléments hors support
type: moc
tags: [reseaux-de-capteurs, complement, moc, transversal]
---

# Le fil rouge de l'énergie

> **Idée directrice du cours.** Sur un nœud capteur, l'énergie est *la* ressource critique, et la radio en est le poste dominant. Presque toutes les décisions techniques du cours découlent de ce seul fait.

Cette note n'introduit aucune notion nouvelle : elle rassemble les endroits où le cours revient sur le même principe, chapitre après chapitre. À lire en fin de parcours, ou comme trame de révision.

## Chapitre 1 — le constat

- [[Unité de communication (transceiver)]] — l'émission coûte cher, **mais l'écoute presque autant**. C'est le point contre-intuitif d'où tout part.
- [[Contraintes des réseaux de capteurs]] — l'énergie est posée comme la première des six contraintes.
- [[Topologie hiérarchique (clusters)]] — la topologie la plus économe est celle qui permet d'agréger.

## Chapitre 2 — l'adressage y répond déjà

- [[6LoWPAN]] — comprimer les en-têtes, c'est transmettre moins d'octets, donc dépenser moins d'énergie. La compression n'est pas une élégance protocolaire, c'est une mesure d'économie.
- [[Types d'adresses IPv6]] — IPv6 supprime le broadcast au profit du multicast, précisément pour ne pas réveiller inutilement tous les nœuds.
- [[SLAAC]] — l'auto-configuration évite un serveur, donc du dialogue, donc des transmissions.

## Chapitre 3 — le choix radio est un choix énergétique

- [[Compromis portée-débit-consommation]] — le triangle : la portée se paie en puissance ou en temps d'antenne.
- [[LoRa et LoRaWAN]] — monter en facteur d'étalement allonge le temps d'antenne, donc l'énergie par message.
- [[RPL]] — le timer Trickle espace les messages de contrôle quand le réseau est stable ; la fonction d'objectif peut prendre l'énergie résiduelle comme critère.
- [[Qualité de lien (PRR, ETX, RSSI, LQI)]] — minimiser l'ETX total revient à minimiser le nombre de transmissions, donc l'énergie.

## Chapitre 4 — la stratégie

- [[Budget énergétique d'un nœud]] — le calcul qui chiffre tout : 5 ans en dormant, 9 jours en écoutant.
- [[Duty cycling]] — le levier le plus puissant, et le plus universel.
- [[Agrégation de données]] — calculer localement pour transmettre moins.
- [[Récupération d'énergie (energy harvesting)]] — changer de logique : équilibrer la consommation avec ce qu'on récolte.

## Compléments — les limites du principe

- [[Couche MAC et accès au canal (CSMA-CA)]] — écouter avant d'émettre suppose d'écouter : l'accès au canal et l'économie d'énergie s'opposent frontalement.
- [[TSCH]] — rendre le rapport cyclique déterministe, au prix d'une synchronisation permanente.
- [[Sécurité des réseaux de capteurs]] — la sécurité coûte des octets à transmettre ; et le *denial of sleep* est une attaque qui vise directement le budget énergétique.

## La question à se poser sur toute décision de conception

> Combien d'octets cela fait-il transmettre, et combien de temps cela laisse-t-il la radio allumée ?

Toutes les réponses du cours se ramènent à ces deux questions.

## Notions liées

- [[Réseau de capteurs sans fil (WSN)]]
- [[Budget énergétique d'un nœud]]
- [[Duty cycling]]
- [[Compromis portée-débit-consommation]]

---
*Complément hors support. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
