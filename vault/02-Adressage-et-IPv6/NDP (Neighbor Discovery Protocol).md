---
title: "NDP (Neighbor Discovery Protocol)"
chapitre: 2 - Adressage et protocole IPv6
type: protocole
tags: [reseaux-de-capteurs, chapitre-2, protocole]
---

# NDP (Neighbor Discovery Protocol)

> **Définition.** Protocole central d'IPv6, transporté par ICMPv6, qui remplace et étend ARP d'IPv4.

- **Découverte des routeurs** : messages Router Solicitation / Router Advertisement (utilisés par SLAAC).
- **Résolution d'adresse** : associer une adresse IPv6 de voisin à son adresse matérielle, via Neighbor Solicitation (NS) / Neighbor Advertisement (NA).
- **Détection d'inaccessibilité de voisin** (NUD).
- **Détection d'adresse dupliquée** (DAD) : garantir l'unicité d'une adresse avant de l'utiliser.

## Notions liées

- [[IPv6]]
- [[SLAAC]]
- [[Types d'adresses IPv6]]

---
*Chapitre 2 — Adressage et protocole IPv6. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
