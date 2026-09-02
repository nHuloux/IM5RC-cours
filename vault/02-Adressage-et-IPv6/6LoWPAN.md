---
title: "6LoWPAN"
chapitre: 2 - Adressage et protocole IPv6
type: protocole
tags: [reseaux-de-capteurs, chapitre-2, protocole]
---

# 6LoWPAN

> **Définition.** IPv6 over Low-power Wireless Personal Area Networks : couche d'adaptation, définie par l'IETF, qui permet de faire transiter des paquets IPv6 sur des réseaux radio contraints de type IEEE 802.15.4.

Tension fondamentale : IPv6 exige une MTU minimale de 1280 octets par lien, alors qu'une trame IEEE 802.15.4 ne fait que 127 octets au total (une centaine d'octets utiles une fois les en-têtes de liaison et la sécurité déduits). Transporter directement une adresse IPv6 (32 octets rien que pour source + destination) est inenvisageable tel quel.

6LoWPAN s'intercale entre la couche liaison (802.15.4) et la couche réseau (IPv6), et apporte trois mécanismes :
- **Compression d'en-tête** : les champs redondants ou déductibles du contexte local sont élidés — un en-tête IPv6 de 40 octets peut être réduit à quelques octets.
- **Fragmentation et réassemblage** : quand un paquet dépasse la capacité d'une trame 802.15.4, il est découpé à l'émission et réassemblé à la réception. L'en-tête de fragmentation coûte 4 octets sur le premier fragment et 5 sur les suivants.
- **Transmission dans le réseau maillé** (*mesh addressing*) : en-tête permettant le relayage multi-saut.

En pratique, un capteur IPv6 moderne empile souvent : IEEE 802.15.4 → 6LoWPAN → IPv6 → UDP → CoAP, avec un routage multi-saut assuré par RPL.

**Exemple.** Sur un même PAN, tous les nœuds partagent le préfixe /64. Plutôt que de répéter ce préfixe (8 octets) dans chaque paquet, 6LoWPAN le déduit du contexte : là où l'en-tête IPv6 brut consommerait la quasi-totalité d'une trame de 127 octets, la version compressée en laisse l'essentiel disponible pour les données utiles.

## Repères chiffrés

Le budget d'octets d'une trame, poste par poste :

| Poste | Sans 6LoWPAN | Avec 6LoWPAN |
|---|---|---|
| Trame PHY 802.15.4 | 127 o | 127 o |
| En-tête MAC + FCS | − 25 o | − 25 o |
| **Charge utile MAC** | **102 o** | **102 o** |
| En-tête IPv6 | − 40 o | − 7 o (IPHC, cas multi-saut) |
| En-tête UDP | − 8 o | − 4 o (NHC) |
| **Données applicatives** | **54 o** | **91 o** |
| Idem avec AES-CCM* (− 21 o) | 33 o | 70 o |

Deux chiffres à retenir : la compression IPHC descend l'en-tête IPv6 à **2 octets** dans le cas le plus favorable (lien local, adresses dérivées de l'EUI-64, octet de dispatch inclus) et à **7 octets** dans le cas multi-saut de référence. La compression NHC ramène l'en-tête UDP de 8 octets à 2 au mieux, 4 lorsque la somme de contrôle est transportée. Avec la sécurité activée, 6LoWPAN **double** la charge utile disponible : 33 → 70 octets.

## Références

- RFC 4919 — cas d'usage et exigences.
- RFC 4944 — transmission d'IPv6 sur 802.15.4, fragmentation, *mesh addressing*.
- RFC 6282 — compression d'en-tête IPHC et NHC.

## Notions liées

- [[IPv6]]
- [[En-tête IPv6]]
- [[IEEE 802.15.4]]
- [[Pile protocolaire de l'IoT contraint]]
- [[RPL]]
- [[Contraintes des réseaux de capteurs]]
- [[Sécurité des réseaux de capteurs]]

---
*Chapitre 2 — Adressage et protocole IPv6. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
