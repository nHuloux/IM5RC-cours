---
title: "IEEE 802.15.4"
chapitre: 3 - La communication dans les réseaux de capteurs
type: technologie
tags: [reseaux-de-capteurs, chapitre-3, technologie]
---

# IEEE 802.15.4

> **Définition.** Norme qui définit les couches physique et liaison des réseaux personnels sans fil basse consommation (LR-WPAN). Bande 2,4 GHz, ~250 kbit/s, portée de quelques dizaines de mètres.

C'est la base sur laquelle se construisent Zigbee et Thread. Sa trame ne fait que 127 octets au total, contrainte majeure qui justifie l'existence de 6LoWPAN pour y faire transiter IPv6.

## Repères chiffrés

| | Valeur |
|---|---|
| Trame PHY maximale | 127 octets |
| Charge utile MAC disponible | 102 octets, ou 81 octets avec AES-CCM* et MIC de 128 bits |
| Bande 2,4 GHz | 250 kbit/s, 16 canaux (numérotés 11 à 26), modulation O-QPSK/DSSS |
| Bande 868 MHz (Europe) | 20 kbit/s en BPSK, ou 100 kbit/s en O-QPSK |
| Période de backoff CSMA-CA | 20 symboles, soit 320 µs à 2,4 GHz et 400 µs à 868 MHz |

## Deux modes de fonctionnement

- **Non-beacon** (`macBeaconOrder = 15`) : accès au canal par CSMA-CA non fenêtré. C'est le mode retenu par Zigbee et par les piles 6LoWPAN, donc celui que l'on rencontre en pratique.
- **Beacon-enabled** : le coordinateur émet des balises qui découpent le temps en *superframes* — période d'accès par contention (CAP) puis période sans contention (CFP) avec créneaux garantis (GTS). Utile quand une latence bornée est exigée.

Le détail de l'accès au canal, et la raison pour laquelle il ne suffit pas, sont traités dans [[Couche MAC et accès au canal (CSMA-CA)]]. La variante à créneaux synchronisés et saut de canal, utilisée dans l'industrie, est [[TSCH]].

## Notions liées

- [[Zigbee]]
- [[Thread]]
- [[6LoWPAN]]
- [[Compromis portée-débit-consommation]]
- [[Comparaison des technologies radio]]
- [[Couche MAC et accès au canal (CSMA-CA)]]
- [[TSCH]]
- [[Sécurité des réseaux de capteurs]]

---
*Chapitre 3 — La communication dans les réseaux de capteurs. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
