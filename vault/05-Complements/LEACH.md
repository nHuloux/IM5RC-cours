---
title: "LEACH"
chapitre: Compléments hors support
type: protocole
tags: [reseaux-de-capteurs, complement, protocole]
---

# LEACH

> **Définition.** Low-Energy Adaptive Clustering Hierarchy : protocole de clustering pour WSN qui fait **tourner** le rôle de chef de cluster entre les nœuds, par tirage aléatoire renouvelé à chaque *round*.

LEACH est la réponse au défaut annoncé dans [[Topologie hiérarchique (clusters)]] : le chef de cluster agrège et transmet plus loin, donc se décharge plus vite. Si le rôle est fixe, le réseau meurt par ses chefs.

## Le cycle

Chaque **round** comporte deux phases.

**Phase de mise en place (setup).**
1. Chaque nœud tire un nombre aléatoire et se déclare chef de cluster si ce nombre passe un seuil qui dépend du nombre de rounds déjà écoulés depuis sa dernière élection.
2. Les chefs élus s'annoncent par diffusion.
3. Chaque nœud restant rejoint le chef qu'il reçoit le mieux.
4. Le chef construit un planning **TDMA** et l'envoie à ses membres.

**Phase de régime établi (steady-state).**
Chaque membre émet dans son créneau TDMA — et dort le reste du temps, ce qui est le gain énergétique principal. Le chef agrège les mesures de son cluster et transmet le résultat directement à la station de base, à puissance plus élevée.

Puis un nouveau round commence, avec de nouveaux chefs.

## Les paramètres et les limites

Le pourcentage souhaité de chefs de cluster est un paramètre du protocole : l'article d'origine retient **5 %** comme valeur optimale pour son modèle.

Limites à connaître :
- L'élection est **aléatoire**, donc ne tient compte ni de l'énergie résiduelle réelle, ni de la position : un nœud presque vide peut être élu, un cluster peut se retrouver sans chef bien placé.
- Le chef transmet **directement** à la station de base : LEACH suppose donc que tout nœud peut l'atteindre, ce qui borne la taille du réseau.
- Le coût de l'élection et de la reconstruction des clusters se paie à chaque round.

Ces limites ont produit une large descendance (LEACH-C, HEED, etc.) qui pondère l'élection par l'énergie restante.

## Référence

W. R. Heinzelman, A. Chandrakasan, H. Balakrishnan, « Energy-Efficient Communication Protocol for Wireless Microsensor Networks », *Proc. 33rd Hawaii International Conference on System Sciences* (HICSS-33), janvier 2000.

**À retenir.** L'idée transposable au-delà de LEACH : quand un rôle coûte cher en énergie, la parade n'est pas de mieux choisir qui le tient, c'est de **le faire tourner**.

## Notions liées

- [[Topologie hiérarchique (clusters)]]
- [[Agrégation de données]]
- [[Budget énergétique d'un nœud]]
- [[Mécanismes de résilience]]

---
*Complément hors support. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
