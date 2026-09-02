---
title: "Compléments hors support"
type: moc
tags: [reseaux-de-capteurs, moc, complement]
---

# Compléments hors support

Ces notions **ne figurent pas dans le support de cours** `26-27_COURS_IPG_INGE_Reseaux-capteurs-IM5RC-Support-complet.tex`. Elles ont été ajoutées au vault parce que le reste du cours les mobilise sans les avoir posées : la pile protocolaire cite CoAP, le duty cycling cite TSCH, la topologie hiérarchique cite LEACH, RPL cite la qualité de lien — et la sécurité n'apparaissait nulle part.

Elles sont regroupées ici plutôt que dispersées dans les quatre chapitres pour rester repérables, et pour que la structure du support reste lisible dans le vault. Si l'une d'elles rejoint le support LaTeX, sa note peut être déplacée dans le chapitre correspondant.

## Les notions

- [[Sécurité des réseaux de capteurs]] — confidentialité, intégrité, disponibilité sous contrainte d'octets et de microampères. AES-CCM\* de 802.15.4, clés LoRaWAN, attaques génériques et attaques RPL, DTLS et OSCORE. **Le manque le plus net du support actuel.**
- [[Couche MAC et accès au canal (CSMA-CA)]] — le problème des collisions, que le cours suppose sans l'énoncer. Prérequis du duty cycling et de TSCH.
- [[CoAP]] — le dernier étage de la pile contrainte, cité dans deux notes sans avoir de page.
- [[Qualité de lien (PRR, ETX, RSSI, LQI)]] — ce que mesure réellement la fonction d'objectif de RPL, et comment valider un déploiement.
- [[TSCH]] — créneaux synchronisés et saut de canal : la variante déterministe de 802.15.4, celle des réseaux industriels.
- [[LEACH]] — la rotation du rôle de chef de cluster, réponse au défaut de la topologie hiérarchique.
- [[Le fil rouge de l'énergie]] — note transversale : tous les endroits où le cours revient sur son principe directeur.

## Rattachement aux chapitres

| Complément | Se greffe sur |
|---|---|
| Sécurité des réseaux de capteurs | chapitres 2, 3 et 4 |
| Couche MAC et accès au canal | chapitres 3 et 4 |
| CoAP | chapitre 2 |
| Qualité de lien | chapitre 3 |
| TSCH | chapitres 3 et 4 |
| LEACH | chapitres 1 et 4 |
| Le fil rouge de l'énergie | les quatre chapitres |

## Voir aussi

- [[Accueil]]
- [[Chapitre 1 - Introduction, architectures et applications]]
- [[Chapitre 2 - Adressage et protocole IPv6]]
- [[Chapitre 3 - La communication dans les réseaux de capteurs]]
- [[Chapitre 4 - Économie d'énergie et tolérance aux pannes]]
