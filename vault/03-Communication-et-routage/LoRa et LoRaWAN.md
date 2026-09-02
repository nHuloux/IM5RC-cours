---
title: "LoRa et LoRaWAN"
chapitre: 3 - La communication dans les réseaux de capteurs
type: technologie
tags: [reseaux-de-capteurs, chapitre-3, technologie]
---

# LoRa et LoRaWAN

> **Définition.** LoRa : modulation longue portée en bande sub-gigahertz libre (868 MHz en Europe), plusieurs kilomètres de portée, débit très faible. LoRaWAN : protocole réseau construit au-dessus, organisé en étoile.

Chaque capteur émet vers des passerelles qui relaient vers un serveur de réseau central. LoRaWAN définit trois classes de terminaux (A, B, C) selon leur compromis réactivité/consommation. C'est la technologie de référence pour les déploiements étendus en extérieur (agriculture, environnement, ville).

**Exemple.** Vignoble étendu : capteurs dispersés sur des hectares, quelques mesures par heure → LoRaWAN (longue portée, très basse consommation, faible débit suffisant). Massif forestier isolé sans couverture : LoRa en réseau privé, éventuellement relais multi-saut.

## Repères chiffrés (région EU868)

| Facteur d'étalement | Débit | Charge utile applicative max |
|---|---|---|
| SF12 (DR0) | 250 bit/s | 51 octets |
| SF11 (DR1) | 440 bit/s | 51 octets |
| SF10 (DR2) | 980 bit/s | 51 octets |
| SF9 (DR3) | 1 760 bit/s | 115 octets |
| SF8 (DR4) | 3 125 bit/s | 222 octets |
| SF7 (DR5) | 5 470 bit/s | 222 octets |
| SF7 / BW250 (DR6) | 11 000 bit/s | 222 octets |

Consommation du transceiver de référence SX1276 : environ **29 mA à +13 dBm** sur la sortie RFO, jusqu'à 120 mA à +20 dBm sur PA_BOOST ; 10,8 mA en réception ; 0,2 µA en sommeil.

## La contrainte qui décide vraiment : le rapport cyclique

En Europe, l'ETSI impose un **rapport cyclique par sous-bande**, indépendamment de la batterie :

| Sous-bande | Rapport cyclique autorisé |
|---|---|
| 863–865 MHz | 0,1 % |
| 868–868,6 MHz (sous-bande principale) | 1 % |
| 869,4–869,65 MHz | 10 % |

**À retenir.** Ce plafond réglementaire, et non l'autonomie, est souvent ce qui limite le nombre de messages par jour. À 1 % dans la sous-bande principale, un message de 1 s de temps d'antenne interdit toute nouvelle émission pendant 99 s sur ce canal. C'est un point de dimensionnement que les projets découvrent en général trop tard : il se calcule avant de choisir la période de mesure, pas après.

Deuxième conséquence, à croiser avec [[Compromis portée-débit-consommation]] : monter en facteur d'étalement pour gagner de la portée allonge le temps d'antenne, donc consomme plus vite le quota de rapport cyclique **et** l'énergie de la pile.

## Notions liées

- [[Topologie en étoile]]
- [[Compromis portée-débit-consommation]]
- [[Comparaison des technologies radio]]
- [[Domaines d'application des WSN]]
- [[Budget énergétique d'un nœud]]
- [[Sécurité des réseaux de capteurs]]

---
*Chapitre 3 — La communication dans les réseaux de capteurs. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
