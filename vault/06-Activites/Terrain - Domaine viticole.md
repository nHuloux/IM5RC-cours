---
title: "Terrain - Domaine viticole"
chapitre: 6 - Activités de transfert
type: terrain
tags: [reseaux-de-capteurs, activite, terrain]
---

# Terrain - Domaine viticole

> **Le terrain en une phrase.** Un domaine de 18 ha éclaté en trois îlots séparés par des routes et un bois, à piloter depuis un chai qui est le seul bâtiment raccordé au courant et au réseau.

## Le contexte

Domaine familial, 18 ha de vignes, conduite en lutte raisonnée. L'exploitant veut
sortir du traitement calendaire et déclencher ses interventions sur des données
plutôt que sur une date.

| Îlot | Surface | Distance au chai | Particularité |
|---|---|---|---|
| A — autour du chai | 6 ha | 0 à 300 m | pente douce, dégagé |
| B — plateau | 7 ha | 1,2 km | ligne de vue partielle, une route entre les deux |
| C — bas de coteau | 5 ha | 2,1 km | bois de 200 m sur l'axe, point bas gélif |

## Ce qu'il faut observer

- **Risque mildiou et oïdium** : température, humidité relative et durée
  d'humectation du feuillage, sous le couvert végétal. C'est la combinaison qui
  alimente le modèle de risque, pas une grandeur isolée.
- **Gel de printemps** : température à 50 cm du sol dans l'îlot C, de mars à mai.
  Une alerte qui arrive après le lever du jour ne sert à rien.
- **État hydrique** : humidité du sol à deux profondeurs, pour décider de
  l'irrigation d'appoint sur l'îlot B.
- **Météo de référence** : une station complète au chai, en appui des points de mesure.

## Ce que le terrain impose

- **Une seule alimentation secteur**, au chai. Tout le reste est sur pile ou sur
  panneau solaire.
- **Le feuillage pousse.** Un lien mesuré en mars, vignes nues, n'est pas le lien
  d'août. Une atténuation saisonnière de plusieurs dB est à prévoir, d'autant plus
  marquée que la fréquence est élevée.
- **Les engins passent.** Rognage, traitements, vendange : tout matériel à moins
  d'un mètre du sol dans le rang sera arraché tôt ou tard.
- **Les nœuds sont accessibles à qui veut.** Une parcelle n'est pas un local
  technique fermé.
- **La maintenance est saisonnière.** L'exploitant accepte une tournée de
  remplacement de piles par an, en hiver. Pas deux.

## Points de départ dans le cours

- [[Domaines d'application des WSN]] — l'agriculture de précision y est le premier cas cité.
- [[Contraintes des réseaux de capteurs]] — les six contraintes, à relire terrain en main.
- [[LoRa et LoRaWAN]] — la famille qui répond aux distances en jeu, avec ses limites.

## Notions liées

- [[Activités de transfert]]
- [[Réseau de capteurs sans fil (WSN)]]
- [[Passerelle (gateway)]]
- [[Récupération d'énergie (energy harvesting)]]

---
*Activités de transfert. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
