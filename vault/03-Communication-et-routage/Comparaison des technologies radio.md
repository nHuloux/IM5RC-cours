---
title: "Comparaison des technologies radio"
chapitre: 3 - La communication dans les réseaux de capteurs
type: concept
tags: [reseaux-de-capteurs, chapitre-3, concept, synthese]
---

# Comparaison des technologies radio

> **Définition.** Tableau de synthèse des cinq familles de technologies radio étudiées, à lire comme un outil de choix plutôt que comme une liste de caractéristiques.

## Le tableau

| Techno | Bande | Débit | Portée | Topologie | Courant en émission | Usage typique |
|---|---|---|---|---|---|---|
| **BLE** | 2,4 GHz, 40 canaux de 2 MHz | 125 kbit/s (Coded S=8) à 2 Mbit/s (LE 2M) | 10 à 100 m | étoile ; mesh depuis 2017 | quelques mA | capteurs corporels, balises |
| **802.15.4** (Zigbee, Thread) | 2,4 GHz, canaux 11 à 26 ; 868 MHz | 250 kbit/s ; 20 à 100 kbit/s en 868 | 10 à 100 m par saut | maillée multi-saut | 7 mA (CC2652R) à 24 mA (CC2538) | domotique, bâtiment, industrie |
| **LoRa / LoRaWAN** | 868 MHz, sous-bande g1 | 250 bit/s (SF12) à 5,5 kbit/s (SF7) ; 11 kbit/s en DR6 | 2 à 15 km | étoile de passerelles | 29 mA à +13 dBm ; 120 mA à +20 dBm | agriculture, environnement, ville |
| **NB-IoT** | LTE, 180 kHz | ≈ 227 kbit/s descendant ; 250 kbit/s montant multi-tone, ≈ 20 kbit/s single-tone | couverture opérateur, bonne pénétration en intérieur | étoile cellulaire | pics de 100 à 200 mA | compteurs enterrés, nœuds fixes |
| **LTE-M** | LTE, 1,4 MHz | ≈ 1 Mbit/s | couverture opérateur | étoile cellulaire | élevé | logistique, mobilité, voix |

## Comment s'en servir

Le tableau ne dit pas quelle technologie est la meilleure — il n'y en a pas. Il sert à écarter, dans l'ordre :

1. **La zone à couvrir** élimine d'abord. Au-delà de quelques centaines de mètres sans relais possible, seuls les LPWAN restent.
2. **Le volume de données** élimine ensuite. Une image, même compressée, sort LoRaWAN du jeu ; quelques octets par heure l'y font entrer.
3. **La disponibilité d'une infrastructure** tranche entre cellulaire et réseau privé : NB-IoT et LTE-M évitent de déployer des passerelles, au prix d'un abonnement et d'une dépendance à la couverture.
4. **La mobilité** écarte NB-IoT, qui ne gère pas le transfert intercellulaire en mode connecté (Release 13) — LTE-M, oui.
5. **La contrainte réglementaire** finit le travail : le rapport cyclique ETSI plafonne le nombre de messages en LoRaWAN, voir [[LoRa et LoRaWAN]].

**À retenir.** Deux erreurs de conception classiques : choisir une technologie sur sa portée annoncée sans vérifier le débit qu'il reste à cette portée, et oublier que le courant d'émission du tableau est un courant de **pic** — c'est le courant moyen, calculé dans [[Budget énergétique d'un nœud]], qui détermine l'autonomie.

## Notions liées

- [[Compromis portée-débit-consommation]]
- [[IEEE 802.15.4]]
- [[Zigbee]]
- [[Thread]]
- [[Bluetooth Low Energy (BLE)]]
- [[LoRa et LoRaWAN]]
- [[NB-IoT et LTE-M]]
- [[Budget énergétique d'un nœud]]

---
*Chapitre 3 — La communication dans les réseaux de capteurs. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
