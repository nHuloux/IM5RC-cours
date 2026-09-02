---
title: "TSCH"
chapitre: Compléments hors support
type: protocole
tags: [reseaux-de-capteurs, complement, protocole]
---

# TSCH

> **Définition.** Time-Slotted Channel Hopping : mode d'accès au canal de IEEE 802.15.4e (2012, intégré à la révision 802.15.4-2015) qui combine des créneaux temporels synchronisés et un saut de canal systématique. C'est le mode retenu pour les réseaux industriels.

TSCH répond aux deux faiblesses de [[Couche MAC et accès au canal (CSMA-CA)]] : la latence non bornée et l'exposition aux interférences sur un canal fixe.

## Les deux idées

**Créneaux synchronisés.** Le temps est découpé en *timeslots* — typiquement 10 ms — regroupés en une *slotframe* qui se répète. Chaque cellule est identifiée par un couple **(décalage de créneau, décalage de canal)**, et l'ordonnancement attribue les cellules aux paires de nœuds. Un nœud sait donc à l'avance quand il émet, quand il écoute, et quand il peut dormir : le rapport cyclique devient **déterministe**, et la latence bornée.

**Saut de canal.** À chaque répétition de la slotframe, la même cellule utilise un canal physique différent, calculé à partir de l'ASN (*Absolute Slot Number*, compteur global partagé) et du décalage de canal. Une interférence permanente sur un canal — un réseau Wi-Fi voisin, par exemple — ne dégrade donc plus qu'une fraction des transmissions au lieu de couper le lien.

## Ce que ça change

| | CSMA-CA non fenêtré | TSCH |
|---|---|---|
| Latence | non bornée | bornée par la slotframe |
| Rapport cyclique | subi | choisi et calculable |
| Interférences | subies sur un canal fixe | diluées par le saut de canal |
| Terminal caché | non résolu | résolu par l'ordonnancement |
| Prérequis | aucun | synchronisation d'horloges, ordonnancement à construire |

Le prix est réel : il faut maintenir la synchronisation entre tous les nœuds, et construire l'ordonnancement — de façon centralisée, ou distribuée.

## Références

- IEEE 802.15.4e (2012), repris dans IEEE 802.15.4-2015.
- RFC 7554 — énoncé du problème 6TiSCH (utiliser TSCH dans l'IoT IPv6).
- RFC 8180 — configuration minimale 6TiSCH.

**À retenir.** TSCH est le point où le WSN cesse d'être « au mieux » pour devenir déterministe. C'est ce qui le rend acceptable en milieu industriel, et c'est pourquoi on le retrouve derrière WirelessHART et ISA100.11a.

## Notions liées

- [[Couche MAC et accès au canal (CSMA-CA)]]
- [[IEEE 802.15.4]]
- [[Duty cycling]]
- [[6LoWPAN]]
- [[RPL]]

---
*Complément hors support. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
