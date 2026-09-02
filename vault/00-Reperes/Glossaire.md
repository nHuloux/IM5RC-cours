---
title: "Glossaire"
type: moc
tags: [reseaux-de-capteurs, glossaire]
---

# Glossaire

Sigles et acronymes clés du cours, avec un lien vers leur notion. Vue condensée du glossaire du support de cours, complétée des sigles introduits par les notes du dossier `05-Complements`.

## Notions du support

- [[6LoWPAN]] — IPv6 over Low-power Wireless Personal Area Networks : couche d'adaptation, définie par l'IETF, qui permet de faire transiter des paquets IPv6 sur des réseaux radio contraints de type IEEE 802.15.4.
- [[Protocoles réactifs (AODV)]] — Protocoles on-demand qui ne calculent une route que lorsqu'un nœud a effectivement quelque chose à envoyer.
- [[Bluetooth Low Energy (BLE)]] — Technologie radio à 2,4 GHz, débit de l'ordre du Mbit/s sur courte portée (quelques mètres à quelques dizaines de mètres), consommation très faible au repos.
- [[Pile protocolaire de l'IoT contraint]] — Empilement protocolaire typique d'un capteur IPv6 moderne : IEEE 802.15.4 → 6LoWPAN → IPv6 → UDP → CoAP, avec RPL pour le routage multi-saut.
- [[RPL]] — Routing Protocol for Low-power and Lossy networks : protocole de routage standardisé par l'IETF pour les réseaux IPv6/6LoWPAN contraints, organisé en arbre orienté (DODAG) enraciné sur la passerelle.
- [[IEEE 802.15.4]] — Norme qui définit les couches physique et liaison des réseaux personnels sans fil basse consommation (LR-WPAN). Bande 2,4 GHz, ~250 kbit/s, portée de quelques dizaines de mètres.
- [[IPv6]] — Protocole d'adressage successeur d'IPv4, sur 128 bits (≈ 3,4 × 10³⁸ adresses), qui permet d'attribuer une adresse unique et publique à chaque objet, même à l'échelle de milliards de capteurs.
- [[LoRa et LoRaWAN]] — LoRa : modulation longue portée en bande sub-gigahertz libre (868 MHz en Europe), plusieurs kilomètres de portée, débit très faible. LoRaWAN : protocole réseau construit au-dessus, organisé en étoile.
- [[NB-IoT et LTE-M]] — Technologies LPWAN cellulaires, appuyées sur les infrastructures des opérateurs mobiles (4G/5G).
- [[Réseau ad-hoc (MANET)]] — Réseau sans fil qui se forme spontanément, sans infrastructure préexistante, les nœuds jouant eux-mêmes le rôle de routeurs. Mobile Ad-hoc NETwork (MANET) quand les nœuds sont mobiles.
- [[Protocoles proactifs (OLSR)]] — Protocoles table-driven qui maintiennent en permanence, dans chaque nœud, une table de routage à jour vers toutes les destinations possibles.
- [[Duty cycling]] — Fait alterner le nœud entre un état actif (radio et capteurs allumés) et un état de sommeil profond, en maximisant le temps de sommeil. Le rapport cyclique (duty cycle) est la fraction de temps passée en état actif.
- [[Récupération d'énergie (energy harvesting)]] — Capter de l'énergie dans l'environnement du nœud pour recharger sa réserve : solaire, cinétique, thermique, ou radiofréquence.
- [[SLAAC]] — StateLess Address AutoConfiguration : mécanisme qui permet à un nœud de se fabriquer lui-même une adresse IPv6, sans serveur central.
- [[Zigbee]] — Pile réseau construite sur IEEE 802.15.4, ajoutant les couches réseau et application avec un routage mesh.
- [[Thread]] — Technologie plus récente, construite sur 802.15.4 et 6LoWPAN, qui offre un maillage IPv6 natif sans point unique de défaillance.
- [[NDP (Neighbor Discovery Protocol)]] — Protocole central d'IPv6, transporté par ICMPv6, qui remplace et étend ARP d'IPv4.
- [[Passerelle (gateway)]] — Nœud particulier (sink/gateway) disposant de plus de ressources (alimentation secteur, liaison Internet, IP publique), qui fait le pont entre le réseau de capteurs et une infrastructure classique.

## Sigles des compléments

- [[CoAP]] — Constrained Application Protocol (RFC 7252) : équivalent allégé de HTTP pour objets contraints, sur UDP, en-tête fixe de 4 octets.
- [[Couche MAC et accès au canal (CSMA-CA)]] — Carrier Sense Multiple Access with Collision **Avoidance** : écouter le canal avant d'émettre, et attendre un délai aléatoire s'il est occupé. Évite les collisions au lieu de les détecter, puisqu'une radio ne peut pas les détecter en émettant.
- [[TSCH]] — Time-Slotted Channel Hopping (IEEE 802.15.4e) : créneaux temporels synchronisés et saut de canal. La variante déterministe, utilisée en milieu industriel.
- [[LEACH]] — Low-Energy Adaptive Clustering Hierarchy : protocole qui fait tourner le rôle de chef de cluster par tirage aléatoire, à chaque *round*.
- [[Qualité de lien (PRR, ETX, RSSI, LQI)]] — **PRR** : taux de trames reçues. **ETX** : nombre attendu de transmissions pour faire passer une trame, métrique par défaut de MRHOF. **RSSI** : puissance reçue, en dBm. **LQI** : indicateur de qualité de modulation de 802.15.4, de 0 à 255.
- [[Sécurité des réseaux de capteurs]] — **AES-CCM\*** : mode de chiffrement authentifié de 802.15.4. **MIC** : code d'intégrité (4, 8 ou 16 octets). **DTLS** : TLS sur UDP (RFC 6347 / 9147). **OSCORE** : sécurité au niveau objet pour CoAP (RFC 8613), qui traverse les proxies. **OTAA / ABP** : les deux modes d'activation LoRaWAN.

## Sigles à connaître sans note dédiée

- **CAN** — convertisseur analogique-numérique, dernier étage de l'[[Unité de captation]].
- **DODAG** — Destination Oriented Directed Acyclic Graph : l'arbre orienté construit par [[RPL]].
- **DIO / DIS / DAO** — les messages de contrôle de [[RPL]] : construction de l'arbre, sollicitation, annonce de destination.
- **IPHC / NHC** — les deux mécanismes de compression d'en-tête de [[6LoWPAN]] (RFC 6282) : en-tête IPv6 et en-tête de niveau supérieur.
- **MTU** — Maximum Transmission Unit : 1280 octets minimum en IPv6, contre 127 octets pour une trame [[IEEE 802.15.4]]. Toute la raison d'être de 6LoWPAN.
- **SF / DR** — facteur d'étalement et *data rate* en [[LoRa et LoRaWAN]] : SF12/DR0 pour la portée, SF7/DR5 pour le débit.
- **LPWAN** — Low-Power Wide-Area Network : la famille longue portée et bas débit (LoRaWAN, NB-IoT, LTE-M).
- **GTS** — Guaranteed Time Slot du mode *beacon-enabled* de 802.15.4, voir [[Couche MAC et accès au canal (CSMA-CA)]].

## Voir aussi

- [[Accueil]]
- [[Compléments hors support]]
