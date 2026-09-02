---
title: "Chapitre 1 - Introduction, architectures et applications"
type: moc
tags: [reseaux-de-capteurs, moc, chapitre-1]
---

# Chapitre 1 - Introduction, architectures et applications

Notions du chapitre 1 — *Introduction, architectures et applications*.

- [[Réseau de capteurs sans fil (WSN)]] — Ensemble de nœuds capteurs autonomes, spatialement distribués, qui coopèrent pour mesurer des grandeurs physiques, traiter localement ces mesures, et les acheminer sans fil de proche en proche jusqu'à une passerelle.
- [[Nœud capteur (mote)]] — Système embarqué contraint constitué de quatre sous-ensembles fonctionnels : unité de captation, de traitement, de communication et d'alimentation.
- [[Unité de captation]] — Sous-ensemble du nœud capteur : un ou plusieurs capteurs, leur conditionnement de signal et un convertisseur analogique-numérique (CAN). L'interface avec le monde physique.
- [[Unité de traitement]] — Microcontrôleur (ARM Cortex-M, ESP32, MSP430...) et sa mémoire, volontairement limités pour économiser l'énergie.
- [[Unité de communication (transceiver)]] — Émetteur-récepteur radio du nœud capteur : de loin le composant le plus gourmand en énergie.
- [[Unité d'alimentation]] — Batterie, pile, ou dispositif de récupération d'énergie (energy harvesting). Conditionne la durée de vie de tout le nœud.
- [[Passerelle (gateway)]] — Nœud particulier (sink/gateway) disposant de plus de ressources (alimentation secteur, liaison Internet, IP publique), qui fait le pont entre le réseau de capteurs et une infrastructure classique.
- [[Topologie en étoile]] — Tous les nœuds communiquent directement avec la passerelle, en un seul saut (single-hop). La topologie la plus simple.
- [[Topologie maillée (mesh)]] — Les nœuds peuvent relayer les messages les uns des autres. L'information chemine en plusieurs sauts (multi-hop) jusqu'à la passerelle.
- [[Topologie hiérarchique (clusters)]] — Les nœuds sont regroupés en clusters ; chaque cluster élit un chef de cluster (cluster head) qui agrège les données de ses membres et les transmet vers la passerelle.
- [[Contraintes des réseaux de capteurs]] — Ce qui distingue un WSN d'un réseau informatique classique : énergie limitée, ressources de calcul/mémoire réduites, bande passante faible, environnement hostile, passage à l'échelle, coût.
- [[Domaines d'application des WSN]] — Les réseaux de capteurs se déploient dès qu'il faut observer un phénomène étendu dans l'espace, en continu, à coût raisonnable.

## Compléments rattachés à ce chapitre

- [[LEACH]] — la rotation du rôle de chef de cluster, qui répond au défaut de la topologie hiérarchique.
- [[Le fil rouge de l'énergie]] — note transversale sur le principe directeur du cours.

## Voir aussi

- [[Accueil]]
- [[Chapitre 2 - Adressage et protocole IPv6]]
- [[Chapitre 3 - La communication dans les réseaux de capteurs]]
- [[Chapitre 4 - Économie d'énergie et tolérance aux pannes]]
- [[Compléments hors support]]
