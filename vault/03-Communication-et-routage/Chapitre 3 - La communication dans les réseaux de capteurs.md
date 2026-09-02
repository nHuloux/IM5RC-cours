---
title: "Chapitre 3 - La communication dans les réseaux de capteurs"
type: moc
tags: [reseaux-de-capteurs, moc, chapitre-3]
---

# Chapitre 3 - La communication dans les réseaux de capteurs

Notions du chapitre 3 — *La communication dans les réseaux de capteurs*.

- [[Compromis portée-débit-consommation]] — Toute communication sans fil repose sur un compromis entre portée, débit, consommation et coût, qu'on ne peut pas tous optimiser en même temps.
- [[Comparaison des technologies radio]] — Tableau de synthèse des cinq familles étudiées, à lire comme un outil de choix : quoi éliminer, et dans quel ordre.
- [[IEEE 802.15.4]] — Norme qui définit les couches physique et liaison des réseaux personnels sans fil basse consommation (LR-WPAN). Bande 2,4 GHz, ~250 kbit/s, portée de quelques dizaines de mètres.
- [[Zigbee]] — Pile réseau construite sur IEEE 802.15.4, ajoutant les couches réseau et application avec un routage mesh.
- [[Thread]] — Technologie plus récente, construite sur 802.15.4 et 6LoWPAN, qui offre un maillage IPv6 natif sans point unique de défaillance.
- [[Bluetooth Low Energy (BLE)]] — Technologie radio à 2,4 GHz, débit de l'ordre du Mbit/s sur courte portée (quelques mètres à quelques dizaines de mètres), consommation très faible au repos.
- [[LoRa et LoRaWAN]] — LoRa : modulation longue portée en bande sub-gigahertz libre (868 MHz en Europe), plusieurs kilomètres de portée, débit très faible. LoRaWAN : protocole réseau construit au-dessus, organisé en étoile.
- [[NB-IoT et LTE-M]] — Technologies LPWAN cellulaires, appuyées sur les infrastructures des opérateurs mobiles (4G/5G).
- [[Nœuds fixes et nœuds mobiles]] — Un nœud fixe, posé une fois, donne une topologie stable ; un nœud mobile rend la topologie dynamique et le routage difficile.
- [[Réseau ad-hoc (MANET)]] — Réseau sans fil qui se forme spontanément, sans infrastructure préexistante, les nœuds jouant eux-mêmes le rôle de routeurs. Mobile Ad-hoc NETwork (MANET) quand les nœuds sont mobiles.
- [[Routage dans les réseaux ad-hoc]] — Détermination du chemin de nœuds relais qu'un paquet doit emprunter pour atteindre sa destination, rendue difficile par une topologie changeante et des ressources rares.
- [[Protocoles proactifs (OLSR)]] — Protocoles table-driven qui maintiennent en permanence, dans chaque nœud, une table de routage à jour vers toutes les destinations possibles.
- [[Protocoles réactifs (AODV)]] — Protocoles on-demand qui ne calculent une route que lorsqu'un nœud a effectivement quelque chose à envoyer.
- [[Protocoles hybrides (ZRP)]] — Combinent les deux approches : proactif à l'intérieur d'une zone locale, réactif au-delà, pour les destinations lointaines et rares.
- [[RPL]] — Routing Protocol for Low-power and Lossy networks : protocole de routage standardisé par l'IETF pour les réseaux IPv6/6LoWPAN contraints, organisé en arbre orienté (DODAG) enraciné sur la passerelle.

## Compléments rattachés à ce chapitre

- [[Couche MAC et accès au canal (CSMA-CA)]] — le problème des collisions, prérequis non énoncé du chapitre.
- [[Qualité de lien (PRR, ETX, RSSI, LQI)]] — ce que mesure réellement la fonction d'objectif de RPL.
- [[TSCH]] — la variante déterministe de 802.15.4, celle des réseaux industriels.
- [[Sécurité des réseaux de capteurs]] — attaques sur le routage, en particulier sur RPL.

## Voir aussi

- [[Accueil]]
- [[Chapitre 1 - Introduction, architectures et applications]]
- [[Chapitre 2 - Adressage et protocole IPv6]]
- [[Chapitre 4 - Économie d'énergie et tolérance aux pannes]]
- [[Compléments hors support]]
