---
title: "Chapitre 2 - Adressage et protocole IPv6"
type: moc
tags: [reseaux-de-capteurs, moc, chapitre-2]
---

# Chapitre 2 - Adressage et protocole IPv6

Notions du chapitre 2 — *Adressage et protocole IPv6*.

- [[IPv4 et pénurie d'adresses]] — Protocole d'adressage historique sur 32 bits (≈ 4,3 milliards d'adresses), aujourd'hui épuisé face à l'explosion des objets connectés.
- [[IPv6]] — Protocole d'adressage successeur d'IPv4, sur 128 bits (≈ 3,4 × 10³⁸ adresses), qui permet d'attribuer une adresse unique et publique à chaque objet, même à l'échelle de milliards de capteurs.
- [[Structure d'une adresse IPv6]] — Adresse de 128 bits écrite en hexadécimal, huit groupes de 16 bits séparés par ':', décomposée en préfixe réseau (64 bits) et identifiant d'interface (64 bits).
- [[Types d'adresses IPv6]] — IPv6 abandonne le broadcast d'IPv4 au profit de trois modes : unicast, multicast et anycast.
- [[SLAAC]] — StateLess Address AutoConfiguration : mécanisme qui permet à un nœud de se fabriquer lui-même une adresse IPv6, sans serveur central.
- [[DHCPv6]] — Version IPv6 du protocole DHCP : un serveur centralise l'attribution des adresses et tient à jour la liste des baux (leases).
- [[En-tête IPv6]] — En-tête simplifié par rapport à IPv4, de 40 octets de taille fixe, pour accélérer le traitement par les routeurs.
- [[NDP (Neighbor Discovery Protocol)]] — Protocole central d'IPv6, transporté par ICMPv6, qui remplace et étend ARP d'IPv4.
- [[6LoWPAN]] — IPv6 over Low-power Wireless Personal Area Networks : couche d'adaptation, définie par l'IETF, qui permet de faire transiter des paquets IPv6 sur des réseaux radio contraints de type IEEE 802.15.4.
- [[Pile protocolaire de l'IoT contraint]] — Empilement protocolaire typique d'un capteur IPv6 moderne : IEEE 802.15.4 → 6LoWPAN → IPv6 → UDP → CoAP, avec RPL pour le routage multi-saut.

## Compléments rattachés à ce chapitre

- [[CoAP]] — le dernier étage de la pile contrainte, cité dans le chapitre sans y avoir de page.
- [[Sécurité des réseaux de capteurs]] — le coût de la sécurité en octets, à croiser avec le budget de trame de 6LoWPAN.

## Voir aussi

- [[Accueil]]
- [[Chapitre 1 - Introduction, architectures et applications]]
- [[Chapitre 3 - La communication dans les réseaux de capteurs]]
- [[Chapitre 4 - Économie d'énergie et tolérance aux pannes]]
- [[Compléments hors support]]
