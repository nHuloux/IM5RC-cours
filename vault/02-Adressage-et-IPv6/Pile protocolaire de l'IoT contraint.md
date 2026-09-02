---
title: "Pile protocolaire de l'IoT contraint"
chapitre: 2 - Adressage et protocole IPv6
type: concept
tags: [reseaux-de-capteurs, chapitre-2, concept]
---

# Pile protocolaire de l'IoT contraint

> **Définition.** Empilement protocolaire typique d'un capteur IPv6 moderne : IEEE 802.15.4 → 6LoWPAN → IPv6 → UDP → CoAP, avec RPL pour le routage multi-saut.

**CoAP** (Constrained Application Protocol) est un équivalent allégé de HTTP pour objets contraints, transporté sur UDP plutôt que TCP pour rester léger. Cette pile complète illustre comment chaque couche résout un problème spécifique de la contrainte radio : la physique et la liaison (802.15.4), l'adressage compressé (6LoWPAN/IPv6), le transport léger (UDP), l'application (CoAP) et le routage vers la passerelle (RPL).

## Schéma

```mermaid
flowchart LR
    subgraph CLASSIQUE["Pile Internet classique"]
        direction TB
        c5[HTTP / TLS] --> c4[TCP] --> c3[IPv4 ou IPv6] --> c1[Ethernet 802.3 / Wi-Fi 802.11]
    end
    subgraph CONTRAINT["Pile IoT contraint"]
        direction TB
        d5[CoAP] --> d4[UDP] --> d3[IPv6] --> d2["6LoWPAN<br/>compression, fragmentation, mesh"] --> d1["IEEE 802.15.4<br/>PHY + MAC, trame de 127 octets"]
        d3 -.- RPL["RPL<br/>routage multi-saut"]
    end
    CLASSIQUE ~~~ CONTRAINT
```

La mise en regard fait apparaître l'essentiel : **6LoWPAN est une couche en plus**, absente de la pile classique, insérée uniquement parce que le lien radio est trop petit pour IPv6. Trois autres substitutions suivent la même logique de frugalité — UDP au lieu de TCP, CoAP au lieu de HTTP, multicast au lieu de broadcast.

## Notions liées

- [[6LoWPAN]]
- [[IPv6]]
- [[IEEE 802.15.4]]
- [[RPL]]
- [[CoAP]]
- [[Couche MAC et accès au canal (CSMA-CA)]]

---
*Chapitre 2 — Adressage et protocole IPv6. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
