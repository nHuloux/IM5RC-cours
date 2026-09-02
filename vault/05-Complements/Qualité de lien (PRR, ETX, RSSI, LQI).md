---
title: "Qualité de lien (PRR, ETX, RSSI, LQI)"
chapitre: Compléments hors support
type: concept
tags: [reseaux-de-capteurs, complement, concept]
---

# Qualité de lien (PRR, ETX, RSSI, LQI)

> **Définition.** Ensemble des métriques qui quantifient la fiabilité d'un lien radio. Elles servent à choisir un parent de routage, à décider d'un placement de nœud, et à diagnostiquer un déploiement.

Le cours parle de « qualité de lien » comme critère de la fonction d'objectif de [[RPL]] sans dire ce qui se mesure. Or c'est mesurable, et c'est ce qu'on lit sur le terrain.

## Les quatre métriques

| Métrique | Ce qu'elle mesure | Unité / plage | Limite |
|---|---|---|---|
| **RSSI** | puissance du signal reçu | dBm, typiquement −100 à −20 | ne dit rien du bruit ni des interférences |
| **LQI** | qualité de la modulation reçue (802.15.4) | entier de 0 à 255 | définition laissée au constructeur, donc peu comparable |
| **PRR** | taux de trames effectivement reçues | 0 à 1, ou % | statistique : demande du temps et du trafic |
| **ETX** | nombre attendu de transmissions pour faire passer une trame | ≥ 1 | ne capte pas l'asymétrie de latence |

**ETX** est la métrique de référence du routage :

> ETX = 1 / (D_f × D_r)

où `D_f` est la probabilité de succès aller et `D_r` la probabilité de succès retour. Un lien parfait vaut 1 ; un lien qui passe une fois sur deux dans chaque sens vaut 4. Sur un chemin multi-saut, les ETX **s'additionnent**, ce qui donne le bon critère : minimiser le nombre total de transmissions, donc l'énergie.

C'est précisément la métrique que la fonction d'objectif **MRHOF** de RPL (RFC 6719) utilise par défaut, en l'absence d'autre métrique annoncée dans le DIO.

## Pourquoi le nombre de sauts est un mauvais critère

Un chemin de 2 sauts sur des liens médiocres (ETX 4 chacun, total 8) coûte plus cher qu'un chemin de 4 sauts sur de bons liens (ETX 1,2 chacun, total 4,8). Router au plus court nombre de sauts pousse justement vers les liens **longs**, donc faibles, donc coûteux en retransmissions. C'est le piège classique du déploiement de WSN, et la raison pour laquelle OF0 (nombre de sauts, RFC 6552) sert surtout de référence pédagogique.

## La zone de transition

Entre la zone où le lien passe presque toujours et celle où il ne passe jamais, il existe une **zone grise** (*transitional region*) où le PRR fluctue fortement d'un instant à l'autre, sans que le RSSI change beaucoup. Elle peut représenter une part importante de la portée nominale.

Conséquence pratique : un lien mesuré une fois à un instant donné n'est pas un lien caractérisé. Deux règles de déploiement en découlent — mesurer le PRR sur une durée, et **ne jamais dimensionner un réseau à la limite de portée annoncée**, mais avec une marge qui place les liens hors de la zone de transition.

**À retenir.** RSSI est instantané et facile, ETX est statistique et pertinent. Un déploiement se valide au PRR mesuré dans le temps, pas au niveau de signal relevé une fois lors de la pose.

## Notions liées

- [[RPL]]
- [[Couche MAC et accès au canal (CSMA-CA)]]
- [[IEEE 802.15.4]]
- [[Topologie maillée (mesh)]]
- [[Contraintes des réseaux de capteurs]]

---
*Complément hors support. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
