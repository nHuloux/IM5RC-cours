---
title: "Activité 1 - Lire un terrain et poser une architecture"
chapitre: 6 - Activités de transfert
type: activite
tags: [reseaux-de-capteurs, activite, chapitre-1]
---

# Activité 1 - Lire un terrain et poser une architecture

> **En une phrase.** Traduire un besoin métier en grandeurs mesurables, puis choisir une topologie et la défendre.

**Durée indicative** : 3 h, en binôme.
**Terrain** : [[Terrain - Domaine viticole]], [[Terrain - Bâtiment intelligent]] ou
[[Terrain - Site industriel]]. Choisissez-en un et gardez-le pour les activités suivantes.
**Appui** : [[Chapitre 1 - Introduction, architectures et applications]].

## Ce que vous devez savoir faire à la fin

- Passer d'un besoin exprimé en langage métier à un tableau de grandeurs, de
  périodes d'échantillonnage et de latences acceptables.
- Situer les quatre unités d'un nœud sur un capteur réel de votre terrain.
- Choisir une topologie par zone et énoncer ce que ce choix vous coûte.

## 1. Parcours de notions

Lisez dans cet ordre. Pour chaque note, la question n'appelle pas une recopie :
elle appelle une réponse formulée avec **votre** terrain.

| Note | La question à vous poser |
|---|---|
| [[Réseau de capteurs sans fil (WSN)]] | La chaîne va du phénomène physique à la décision. Sur votre terrain, qui prend la décision, et où s'arrête le réseau de capteurs ? |
| [[Domaines d'application des WSN]] | Votre terrain y est cité. Qu'est-ce que la note ne dit pas de votre cas particulier ? |
| [[Contraintes des réseaux de capteurs]] | Classez les six contraintes de la plus mordante à la plus indolore **sur votre terrain**. Deux terrains différents ne donnent pas le même classement. |
| [[Nœud capteur (mote)]] | Prenez un point de mesure concret et nommez ses quatre unités. |
| [[Unité de captation]] · [[Unité de traitement]] · [[Unité de communication (transceiver)]] · [[Unité d'alimentation]] | Laquelle domine la consommation, et pourquoi le résultat est-il contre-intuitif ? |
| [[Passerelle (gateway)]] | Où la placeriez-vous, et qu'est-ce qui tombe avec elle ? |
| [[Topologie en étoile]] · [[Topologie maillée (mesh)]] · [[Topologie hiérarchique (clusters)]] | Les trois schémas se lisent ensemble. Lequel supporte le mieux la géométrie de votre terrain ? |

## 2. Transfert sur le terrain

### 2.1 Cartographier

Dessinez le terrain à l'échelle, même grossièrement. Y faire figurer : les zones,
la distance la plus longue à couvrir, les obstacles, les points où le courant est
disponible, et le nombre de points de mesure par zone.

### 2.2 Le tableau des grandeurs

C'est la pièce maîtresse de l'activité. Une ligne par grandeur observée :

| Grandeur | Pourquoi on la mesure | Période d'échantillonnage | Latence acceptable | Octets utiles par message |
|---|---|---|---|---|

Trois pièges vous attendent, un par terrain :

- **Viticole** — le risque mildiou ne se lit pas sur une grandeur mais sur une
  **combinaison** température / humidité / humectation. Une alerte gel, elle,
  a une latence utile qui se compte en minutes, pas en heures.
- **Bâtiment** — la présence est un **événement**, pas une mesure périodique.
  Un capteur qui envoie « occupé » toutes les dix minutes ne répond pas au besoin,
  et un capteur qui envoie à chaque mouvement en produit bien trop.
- **Industriel** — la vibration utile s'échantillonne à plusieurs kilohertz.
  Confrontez ce débit brut aux ordres de grandeur de
  [[Contraintes des réseaux de capteurs]] : la conclusion doit vous amener à
  changer quelque chose dans l'architecture, pas à choisir une radio plus rapide.

### 2.3 Choisir une topologie, par zone

Pour chaque zone, une topologie et **trois lignes de justification** : ce qu'elle
apporte ici, ce qu'elle coûte ici, ce qui la ferait échouer ici. Un terrain peut
parfaitement mélanger deux topologies — dites alors où passe la frontière.

### 2.4 Le point unique de défaillance

Identifiez-le et chiffrez ce qu'on perd s'il tombe : combien de points de mesure
deviennent muets, et pendant combien de temps compte tenu de la maintenance que
votre terrain autorise.

## 3. Livrable

Quatre pages maximum : le plan annoté, le tableau des grandeurs, le choix de
topologie par zone avec ses justifications, et le paragraphe sur le point unique
de défaillance.

## Critères de réussite

- Chaque période d'échantillonnage est justifiée par la physique du phénomène ou
  par l'usage, jamais par « c'est une valeur courante ».
- Le classement des contraintes est **propre à votre terrain** et argumenté.
- Le choix de topologie énonce un coût, pas seulement un avantage.
- Aucune technologie radio n'est nommée. C'est volontaire : ce choix se prépare
  et se fait à l'activité suivante.

## Pièges fréquents

- Confondre la grandeur mesurée et l'information utile — la température n'est pas
  le risque de gel, elle en est un ingrédient.
- Sur-échantillonner « pour avoir de la marge » : chaque mesure se paiera en
  énergie, et vous en ferez le calcul plus tard.
- Choisir le maillage par réflexe. Relisez les inconvénients dans
  [[Topologie maillée (mesh)]] avant de vous décider.

## Pour aller plus loin

- [[Nœuds fixes et nœuds mobiles]] — si votre terrain comporte des points mobiles.
- [[Glossaire]] — pour fixer le vocabulaire avant la restitution.

## Notions liées

- [[Activités de transfert]]
- [[Activité 2 - Choisir une technologie radio sous contrainte]]
- [[Chapitre 1 - Introduction, architectures et applications]]

---
*Activités de transfert. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
