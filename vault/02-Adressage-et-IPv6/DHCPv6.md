---
title: "DHCPv6"
chapitre: 2 - Adressage et protocole IPv6
type: protocole
tags: [reseaux-de-capteurs, chapitre-2, protocole]
---

# DHCPv6

> **Définition.** Version IPv6 du protocole DHCP : un serveur centralise l'attribution des adresses et tient à jour la liste des baux (leases).

- **DHCPv6 avec état** (*stateful*) : le serveur attribue l'adresse complète et mémorise l'association — contrôle centralisé et traçabilité.
- **DHCPv6 sans état** (*stateless*) : l'adresse est obtenue par SLAAC, DHCPv6 ne fournissant que des informations complémentaires (serveur DNS, NTP...).

**À retenir.** SLAAC est autonome, léger, sans serveur : idéal pour un grand parc de capteurs homogènes. DHCPv6 avec état offre contrôle et traçabilité centralisés, au prix d'un serveur à maintenir. Les deux peuvent coexister.

## Notions liées

- [[IPv6]]
- [[SLAAC]]

---
*Chapitre 2 — Adressage et protocole IPv6. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
