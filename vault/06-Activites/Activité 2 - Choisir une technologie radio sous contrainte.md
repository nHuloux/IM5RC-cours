---
title: "Activité 2 - Choisir une technologie radio sous contrainte"
chapitre: 6 - Activités de transfert
type: activite
tags: [reseaux-de-capteurs, activite, chapitre-3]
---

# Activité 2 - Choisir une technologie radio sous contrainte

> **En une phrase.** Appliquer une méthode d'élimination à un cas réel, et assumer ce qu'on perd en éliminant.

**Durée indicative** : 3 h, en binôme.
**Prérequis** : le tableau des grandeurs et le plan produits en
[[Activité 1 - Lire un terrain et poser une architecture]].
**Appui** : [[Chapitre 3 - La communication dans les réseaux de capteurs]].

## Ce que vous devez savoir faire à la fin

- Dérouler la méthode d'élimination de [[Comparaison des technologies radio]] sur
  un cas qui n'est pas dans le cours.
- Chiffrer un volume de données quotidien et le confronter à une contrainte
  réglementaire.
- Dimensionner avec une marge, et dire laquelle.

## 1. Parcours de notions

| Note | La question à vous poser |
|---|---|
| [[Compromis portée-débit-consommation]] | Le quadrant en haut à droite est vide. Sur votre terrain, quelle grandeur êtes-vous prêt à sacrifier en premier ? |
| [[Comparaison des technologies radio]] | Les cinq critères d'élimination sont **ordonnés**. Pourquoi cet ordre-là, et non l'inverse ? |
| [[IEEE 802.15.4]] · [[Zigbee]] · [[Thread]] | Trois noms pour une même couche basse. Qu'est-ce qui les distingue vraiment ? |
| [[Bluetooth Low Energy (BLE)]] | Que change le mesh de 2017 pour votre terrain ? |
| [[LoRa et LoRaWAN]] | Le rapport cyclique réglementaire : combien de messages par jour, réellement ? |
| [[NB-IoT et LTE-M]] | À quoi renoncez-vous en dépendant d'un opérateur ? |
| [[Nœuds fixes et nœuds mobiles]] | Un seul des cinq candidats gère mal la mobilité. Lequel, et est-ce que cela vous concerne ? |
| [[Qualité de lien (PRR, ETX, RSSI, LQI)]] | La zone de transition : pourquoi la portée annoncée n'est **jamais** la portée de dimensionnement ? |

## 2. Transfert sur le terrain

### 2.1 Dérouler l'élimination, dans l'ordre, par écrit

Reprenez les cinq critères de [[Comparaison des technologies radio]] et tenez la
trace de l'élimination. Une ligne par critère, et à chaque ligne : qui sort, et
pour quelle raison chiffrée.

| Critère | Ce que votre terrain impose | Technologies éliminées | Motif chiffré |
|---|---|---|---|
| 1 · Zone à couvrir | | | |
| 2 · Volume de données | | | |
| 3 · Infrastructure disponible | | | |
| 4 · Mobilité | | | |
| 5 · Contrainte réglementaire | | | |

Une élimination sans chiffre n'est pas une élimination : c'est une préférence.

### 2.2 Calculer le volume réellement transporté

À partir de votre tableau des grandeurs, calculez, par zone : les octets utiles
par message, le nombre de messages par jour et par nœud, puis le total agrégé qui
arrive à la passerelle à l'heure la plus chargée.

Confrontez ce total à la ligne « débit » de [[Comparaison des technologies radio]].
Attention : un débit nominal partagé entre 300 nœuds n'est pas un débit par nœud.

### 2.3 Le contrôle de réalité propre à votre terrain

- **Viticole** — l'îlot C est à 2,1 km derrière un bois. Vérifiez que la
  technologie retenue tient cette distance **au débit qu'il vous faut**, pas au
  débit minimal du tableau. Puis reposez-vous la question en août, feuillage
  développé : que devient votre marge ?
- **Bâtiment** — 350 nœuds dans un volume restreint, et le 2,4 GHz déjà occupé par
  le Wi-Fi. Le facteur limitant n'est pas la portée : cherchez-le du côté du
  partage du canal, et notez ce qu'il faudra vérifier dans
  [[Couche MAC et accès au canal (CSMA-CA)]].
- **Industriel** — écrivez la latence maximale tolérée pour une alarme, en
  secondes. Puis vérifiez, technologie par technologie, laquelle peut la tenir.
  Le rapport cyclique de [[LoRa et LoRaWAN]] doit vous faire éliminer un candidat
  sur ce seul critère.

### 2.4 Poser la marge de dimensionnement

Énoncez la distance ou l'atténuation maximale que vous retenez pour le
dimensionnement, et l'écart que vous gardez avec la portée annoncée. Justifiez
cet écart avec la zone de transition décrite dans
[[Qualité de lien (PRR, ETX, RSSI, LQI)]], et dites comment vous le vérifieriez sur
site — quelle métrique, mesurée pendant combien de temps.

### 2.5 Conclure

Une technologie par zone. Rien n'interdit d'en retenir deux sur un même terrain :
dans ce cas, dites où passe la frontière et ce qui traverse.

## 3. Livrable

Le tableau d'élimination rempli, le calcul de volume, la marge de dimensionnement
avec sa méthode de vérification, et une conclusion d'une demi-page par zone.

## Critères de réussite

- Chaque élimination porte un chiffre.
- Le volume de données est calculé, pas estimé au doigt mouillé.
- La marge de dimensionnement est explicite et justifiée par la zone de transition.
- Vous savez dire ce que votre choix **rend impossible** sur ce terrain.

## Pièges fréquents

Les deux erreurs classiques sont nommées dans [[Comparaison des technologies radio]] :
retenir une technologie sur sa portée annoncée sans vérifier le débit restant à
cette portée, et confondre le courant de pic du tableau avec la consommation
moyenne. La seconde vous rattrapera à l'activité 4.

## Notions liées

- [[Activités de transfert]]
- [[Activité 1 - Lire un terrain et poser une architecture]]
- [[Activité 3 - Faire circuler l'information]]
- [[Chapitre 3 - La communication dans les réseaux de capteurs]]

---
*Activités de transfert. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
