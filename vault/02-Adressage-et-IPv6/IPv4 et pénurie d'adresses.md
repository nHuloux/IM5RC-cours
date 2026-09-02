---
title: "IPv4 et pénurie d'adresses"
chapitre: 2 - Adressage et protocole IPv6
type: concept
tags: [reseaux-de-capteurs, chapitre-2, concept]
---

# IPv4 et pénurie d'adresses

> **Définition.** Protocole d'adressage historique sur 32 bits (≈ 4,3 milliards d'adresses), aujourd'hui épuisé face à l'explosion des objets connectés.

L'adresse IP identifie de façon unique une interface réseau et permet le routage des paquets. IPv4 note ses adresses en décimal pointé (ex. 192.168.1.10). Avec plusieurs dizaines de milliards d'objets connectés estimés, IPv4 ne peut structurellement pas leur attribuer une adresse à chacun. Le NAT (Network Address Translation) partage une adresse publique entre plusieurs machines mais complique la communication de bout en bout : un serveur ne peut pas facilement initier un dialogue vers un objet caché derrière un NAT — problème pour piloter un actionneur ou interroger un capteur à la demande.

## Notions liées

- [[IPv6]]

---
*Chapitre 2 — Adressage et protocole IPv6. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
