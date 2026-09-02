---
title: "Couche MAC et accès au canal (CSMA-CA)"
chapitre: Compléments hors support
type: concept
tags: [reseaux-de-capteurs, complement, concept]
---

# Couche MAC et accès au canal (CSMA-CA)

> **Définition.** La couche MAC arbitre l'accès à un canal radio partagé entre plusieurs nœuds. En IEEE 802.15.4, cet arbitrage repose sur CSMA-CA : écouter avant d'émettre, et attendre un délai aléatoire en cas de canal occupé.

C'est la brique que le cours suppose sans l'énoncer : le [[Duty cycling]] et [[TSCH]] n'ont de sens que si l'on a d'abord posé le problème des **collisions**.

## Le problème

Une radio ne peut pas émettre et recevoir en même temps, et deux nœuds qui émettent simultanément dans la même zone produisent une **collision** : les deux trames sont perdues. Contrairement à Ethernet, une radio ne peut pas détecter la collision pendant qu'elle émet — d'où le « CA », *Collision Avoidance* : on cherche à les **éviter** plutôt qu'à les détecter.

## CSMA-CA en 802.15.4

Le mécanisme, dans le mode non fenêtré (*unslotted*), le plus courant en pratique :

1. Tirer un délai d'attente aléatoire dans `[0, 2^BE − 1]` périodes de backoff.
2. Attendre ce délai.
3. Écouter le canal (CCA, *Clear Channel Assessment*).
4. Si le canal est libre, émettre. Sinon, incrémenter `BE` et recommencer.
5. Au bout de `macMaxCSMABackoffs` échecs, abandonner et remonter l'échec à la couche supérieure.

| Paramètre | Valeur par défaut |
|---|---|
| `macMinBE` — exposant de backoff initial | 3 |
| `macMaxBE` — exposant maximal | 5 |
| `macMaxCSMABackoffs` | 4 |
| `aUnitBackoffPeriod` | 20 symboles, soit 320 µs à 2,4 GHz et 400 µs à 868 MHz |

## Deux modes, deux compromis

- **Non-beacon** (`macBeaconOrder = 15`) : CSMA-CA non fenêtré, pas de synchronisation. Simple, mais latence non bornée. C'est le mode de Zigbee et des piles 6LoWPAN.
- **Beacon-enabled** : le coordinateur découpe le temps en *superframes* — une balise, puis une période d'accès par contention (CAP) en CSMA-CA fenêtré, puis une période sans contention (CFP) où des créneaux garantis (GTS) sont réservés à des nœuds nommés. Latence bornée pour les nœuds qui ont un GTS, au prix d'une synchronisation permanente sur les balises.

## Deux limites à connaître

**Le terminal caché.** Deux nœuds A et C hors de portée l'un de l'autre, mais tous deux à portée de B : leurs CCA se déclarent libres, ils émettent, et B ne reçoit qu'une collision. 802.15.4 **n'implémente pas RTS/CTS**, donc ne résout pas ce problème au niveau MAC. C'est un argument fort pour les approches à créneaux comme [[TSCH]].

**L'incompatibilité avec le sommeil.** CSMA-CA suppose un récepteur à l'écoute. Or un nœud en duty cycling dort. Deux réponses, deux coûts :

| Approche | Le coût est porté par | Coût |
|---|---|---|
| *Low-Power Listening* — le récepteur échantillonne le canal | l'émetteur | préambule long, couvrant la période de réveil |
| Ordonnancement synchronisé (S-MAC, TSCH) | tous les nœuds | synchronisation d'horloges, donc trafic de contrôle |

**À retenir.** L'accès au canal et l'économie d'énergie tirent dans des directions opposées : écouter avant d'émettre suppose d'écouter, et écouter est le poste dominant du [[Budget énergétique d'un nœud]]. Tout protocole MAC de WSN est un arbitrage entre ces deux exigences.

## Notions liées

- [[IEEE 802.15.4]]
- [[Duty cycling]]
- [[TSCH]]
- [[Budget énergétique d'un nœud]]
- [[Qualité de lien (PRR, ETX, RSSI, LQI)]]
- [[Pile protocolaire de l'IoT contraint]]

---
*Complément hors support. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
