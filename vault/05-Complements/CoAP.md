---
title: "CoAP"
chapitre: Compléments hors support
type: protocole
tags: [reseaux-de-capteurs, complement, protocole]
---

# CoAP

> **Définition.** Constrained Application Protocol (RFC 7252) : protocole applicatif de type REST pour objets contraints, transporté sur UDP, avec un en-tête fixe de 4 octets. L'équivalent allégé de HTTP.

CoAP est le dernier étage de la [[Pile protocolaire de l'IoT contraint]]. Il reprend le modèle de HTTP — des ressources identifiées par URI, manipulées par des méthodes — mais en supprimant tout ce qui ne tient pas dans une trame de 127 octets.

## Ce qui change par rapport à HTTP

| | HTTP/1.1 | CoAP |
|---|---|---|
| Transport | TCP | UDP |
| En-tête | textuel, quelques centaines d'octets | binaire, 4 octets fixes |
| Fiabilité | assurée par TCP | optionnelle, gérée par CoAP lui-même |
| Découverte de ressources | hors protocole | `/.well-known/core` |
| Notification de changement | polling ou WebSocket | *Observe* |
| Sécurité | TLS | DTLS ou OSCORE |
| Port par défaut | 80 / 443 | 5683 / 5684 (coaps) |

Le choix d'UDP est le point clé : établir une connexion TCP demande trois échanges avant la première donnée utile, ce qui est prohibitif quand chaque transmission radio est le poste énergétique dominant.

## Les quatre types de messages

| Type | Sigle | Comportement |
|---|---|---|
| Confirmable | CON | retransmis avec repli exponentiel jusqu'à réception d'un ACK |
| Non-confirmable | NON | émis une fois, sans garantie — pour une mesure périodique qu'un autre relèvement remplacera |
| Acquittement | ACK | confirme un CON |
| Reset | RST | signale un message reçu mais non traitable |

CoAP reconstruit ainsi, en quelques octets, une fiabilité **à la carte** : c'est l'application qui décide message par message si la retransmission vaut son coût énergétique.

## Deux extensions indispensables aux capteurs

- **Observe** (RFC 7641) : le client s'abonne à une ressource, le serveur pousse une notification à chaque changement. Cela remplace le *polling*, donc supprime des transmissions inutiles — un gain énergétique direct.
- **Transfert par blocs** (RFC 7959) : découpe une représentation trop grosse pour une trame en une série de blocs numérotés, au niveau applicatif. À ne pas confondre avec la fragmentation de [[6LoWPAN]], qui opère à la couche d'adaptation : le découpage par blocs est plus robuste, car la perte d'un bloc ne condamne pas tout le message.

**À retenir.** CoAP applique au niveau applicatif la même logique que 6LoWPAN au niveau réseau : garder le modèle (REST, IPv6) et supprimer le poids. Sa vraie valeur pour un WSN n'est pas d'être « du HTTP en petit », c'est de rendre la fiabilité et la notification **négociables**, donc facturables en énergie.

## Notions liées

- [[Pile protocolaire de l'IoT contraint]]
- [[6LoWPAN]]
- [[IPv6]]
- [[Sécurité des réseaux de capteurs]]

---
*Complément hors support. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
