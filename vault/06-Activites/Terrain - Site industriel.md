---
title: "Terrain - Site industriel"
chapitre: 6 - Activités de transfert
type: terrain
tags: [reseaux-de-capteurs, activite, terrain]
---

# Terrain - Site industriel

> **Le terrain en une phrase.** Une halle de production en 3×8 où l'on veut anticiper les pannes machines, dans un environnement métallique et électriquement bruyant, avec des alarmes qui ne supportent pas la latence.

## Le contexte

PMI de mécanique, halle de production de 5 000 m² et une zone de stockage
extérieure. Objectif affiché : passer de la maintenance curative à la maintenance
prédictive sur le parc de machines tournantes, et suivre la consommation par
équipement pour le bilan énergétique réglementaire.

| Zone | Étendue | Particularité |
|---|---|---|
| Halle de production | 5 000 m², 9 m sous ferme | charpente et bardage métalliques, ponts roulants |
| Ligne d'assemblage | 120 m linéaires | chariots automatisés en circulation |
| Stockage extérieur | 3 000 m² | non couvert, à 250 m de la halle |
| Local technique | — | armoires électriques, variateurs de fréquence |

## Ce qu'il faut observer

- **Vibration sur machines tournantes** : 40 moteurs et réducteurs. C'est
  l'indicateur précoce du défaut de roulement ou de balourd. Un signal de
  vibration utile s'échantillonne à plusieurs kilohertz — à confronter d'emblée
  avec les débits du cours.
- **Température de paliers et d'armoires** : dérive lente, échantillonnage lâche.
- **Consommation électrique par machine** : sous-comptage, pas de temps réel.
- **Alarmes de sécurité** : dépassement de seuil critique sur une machine. Le
  délai entre le dépassement et l'affichage en supervision est contractuel.

## Ce que le terrain impose

- **Une charpente métallique et des machines en acier.** Réflexions multiples,
  évanouissements profonds, et un lien qui peut se dégrader parce qu'un chariot
  s'est garé au mauvais endroit.
- **Du bruit électromagnétique.** Variateurs de fréquence et soudage rayonnent
  large. Les interférences ne sont pas une hypothèse, c'est le régime permanent.
- **Une exigence de latence** sur les alarmes, à chiffrer et à tenir. Toutes les
  technologies du cours n'en sont pas capables, et certaines s'en interdisent par
  réglementation.
- **Des équipements mobiles** : chariots automatisés, et capteurs déplacés d'une
  machine à l'autre lors des campagnes de mesure.
- **Une production en 3×8.** Il n'y a pas de fenêtre d'arrêt confortable pour
  intervenir, et un arrêt de ligne se chiffre à l'heure.
- **Le site est déjà câblé** en partie, mais tirer un câble jusqu'à une machine
  déplaçable coûte plus cher que le capteur.

## Points de départ dans le cours

- [[Domaines d'application des WSN]] — l'industrie 4.0 et la maintenance prédictive y sont citées.
- [[Nœuds fixes et nœuds mobiles]] — la mobilité change la donne, dès le choix radio.
- [[TSCH]] — la réponse historique du monde industriel au bruit et au déterminisme.

## Notions liées

- [[Activités de transfert]]
- [[Agrégation de données]]
- [[Qualité de lien (PRR, ETX, RSSI, LQI)]]
- [[Tolérance aux pannes]]

---
*Activités de transfert. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
