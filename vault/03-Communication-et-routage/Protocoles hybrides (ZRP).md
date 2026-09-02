---
title: "Protocoles hybrides (ZRP)"
chapitre: 3 - La communication dans les réseaux de capteurs
type: protocole
tags: [reseaux-de-capteurs, chapitre-3, protocole]
---

# Protocoles hybrides (ZRP)

> **Définition.** Combinent les deux approches : proactif à l'intérieur d'une zone locale, réactif au-delà, pour les destinations lointaines et rares.

Exemple : **ZRP** (Zone Routing Protocol). L'idée est de profiter de la faible latence du proactif là où les routes servent souvent (le voisinage immédiat), tout en évitant le coût permanent du proactif pour des destinations lointaines et rarement sollicitées.

**Statut à connaître.** Contrairement à AODV (RFC 3561) et OLSR (RFC 3626), ZRP n'a **jamais été publié en RFC** : le document IETF correspondant est resté à l'état de draft et a expiré en 2002. C'est une précision utile — elle explique pourquoi les protocoles hybrides restent surtout une catégorie conceptuelle, commode pour classer les approches, plutôt qu'un choix d'ingénierie que l'on rencontre sur le terrain. Dans l'IoT contraint, la place qu'ils visaient est occupée par [[RPL]].

## Notions liées

- [[Routage dans les réseaux ad-hoc]]
- [[Protocoles proactifs (OLSR)]]
- [[Protocoles réactifs (AODV)]]
- [[RPL]]

---
*Chapitre 3 — La communication dans les réseaux de capteurs. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
