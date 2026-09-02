---
title: "Activité 4 - Tenir dans la durée"
chapitre: 6 - Activités de transfert
type: activite
tags: [reseaux-de-capteurs, activite, chapitre-4]
---

# Activité 4 - Tenir dans la durée

> **En une phrase.** Chiffrer une autonomie, la confronter à la maintenance que le terrain autorise, puis regarder ce qui peut casser ou être attaqué.

**Durée indicative** : 3 h, en binôme.
**Prérequis** : la technologie et la pile retenues aux activités 2 et 3.
**Appui** : [[Chapitre 4 - Économie d'énergie et tolérance aux pannes]] et
[[Compléments hors support]].

## Ce que vous devez savoir faire à la fin

- Conduire un calcul d'autonomie complet et interpréter la répartition de la charge.
- Décider ce qui se calcule dans le nœud plutôt que sur le serveur, et le justifier en octets.
- Construire une table de menaces propre à un terrain, et distinguer ce que la cryptographie règle de ce qu'elle ne règle pas.

## 1. Parcours de notions

| Note | La question à vous poser |
|---|---|
| [[Le fil rouge de l'énergie]] | À lire en premier. Deux questions y résument tout le cours : lesquelles ? |
| [[Budget énergétique d'un nœud]] | 5 ans en dormant, 9 jours en écoutant. D'où vient exactement le facteur 200 ? |
| [[Duty cycling]] | Quel rapport cyclique votre terrain vous autorise-t-il, compte tenu de la latence exigée en activité 1 ? |
| [[Agrégation de données]] | Qu'est-ce qui peut se calculer dans le nœud sur votre terrain ? |
| [[Récupération d'énergie (energy harvesting)]] | Pertinent chez vous, ou gadget ? Justifiez dans les deux cas. |
| [[Couche MAC et accès au canal (CSMA-CA)]] | Écouter avant d'émettre suppose d'écouter. Comment cette contradiction se règle-t-elle ? |
| [[TSCH]] | Ce qu'il achète, ce qu'il impose. |
| [[Tolérance aux pannes]] · [[Mécanismes de résilience]] | Quels modes de défaillance sont plausibles chez vous ? |
| [[LEACH]] | Si vous avez retenu une topologie en clusters : pourquoi faire tourner le rôle de chef ? |
| [[Sécurité des réseaux de capteurs]] | Quelles attaques de la liste sont crédibles sur votre terrain, et lesquelles ne le sont pas ? |

## 2. Transfert sur le terrain

### 2.1 Le budget énergétique, chiffré

Prenez le nœud le plus sollicité de votre terrain et refaites, avec vos valeurs, le
tableau de [[Budget énergétique d'un nœud]] :

| État | Courant | Durée par cycle | Charge |
|---|---|---|---|
| Sommeil profond | | | |
| Mesure | | | |
| Émission | | | |
| Réception / écoute | | | |
| **Total sur un cycle** | | | |

Puis I_moy, puis T_vie. Prenez vos courants dans une fiche technique réelle du
composant que vous envisagez, et citez-la.

**Le résultat doit être confronté à la maintenance que votre terrain autorise** :
une tournée par an au domaine viticole, une intervention facturée au bâtiment,
pas de fenêtre d'arrêt confortable en 3×8. Si l'autonomie calculée ne tient pas,
ne changez pas la pile en premier : changez une décision prise plus tôt, et dites
laquelle.

### 2.2 Deux variantes à calculer

Refaites le calcul dans deux cas, et commentez l'écart :

1. La période d'échantillonnage est divisée par quatre — le métier veut « plus fin ».
2. Il faut gagner de la portée : facteur d'étalement supérieur en LoRa, ou puissance
   d'émission supérieure. [[Compromis portée-débit-consommation]] annonce la couleur,
   à vous de la chiffrer.

### 2.3 Ce qui se calcule dans le nœud

Décidez, grandeur par grandeur, ce qui remonte brut et ce qui remonte agrégé, et
chiffrez l'économie en octets par jour.

- **Viticole** — min / max / moyenne horaires suffisent pour le suivi, mais l'alerte
  gel doit partir immédiatement. Deux régimes de trafic coexistent : décrivez-les.
- **Bâtiment** — l'envoi sur franchissement de seuil plutôt que périodique change
  le volume d'un ordre de grandeur. Que se passe-t-il alors quand un capteur est
  simplement mort, et comment le distinguez-vous d'un capteur silencieux parce que
  rien n'a changé ?
- **Industriel** — le signal de vibration brut ne remonte pas. Décidez quels
  indicateurs sont extraits localement, et dites ce que vous perdez définitivement
  en ne conservant pas le signal brut.

### 2.4 Ce qui casse

Une ligne par mode de défaillance plausible : ce qui tombe, comment on s'en aperçoit,
en combien de temps, et ce qu'on a prévu. Traitez au minimum la panne de passerelle,
la panne d'un relais, et le nœud qui se met à mentir sans tomber.

### 2.5 La table des menaces

Reprenez la liste d'attaques de [[Sécurité des réseaux de capteurs]] et gardez
celles qui sont crédibles chez vous. Pour chacune : plausibilité, impact, parade,
et **coût de la parade en octets** — à reporter sur le budget de trame de
l'activité 3.

Chaque terrain a sa menace signature : nœuds physiquement accessibles dans les
vignes, données de présence nominatives dans le bâtiment, alarme de sécurité
silencieusement filtrée en usine. Traitez la vôtre en priorité, et rappelez ce que
le chiffrement **ne** protège **pas**.

## 3. Livrable

Le calcul d'autonomie avec ses sources, les deux variantes commentées, la décision
d'agrégation chiffrée, la table des modes de défaillance et la table des menaces.

## Critères de réussite

- Les courants viennent d'une fiche technique citée, pas d'un ordre de grandeur mémorisé.
- L'autonomie est confrontée à la contrainte de maintenance, et l'écart est assumé.
- L'économie d'agrégation est exprimée en octets par jour.
- La table des menaces distingue ce qui relève de la cryptographie et ce qui relève de la redondance.

## Pièges fréquents

- Traiter l'énergie en fin de conception. Relisez [[Le fil rouge de l'énergie]] :
  presque toutes vos décisions précédentes étaient déjà des décisions énergétiques.
- Oublier le coût de l'écoute et ne compter que l'émission.
- Croire qu'un nœud chiffré est un nœud disponible : le brouillage et le
  *denial of sleep* passent à travers.

## Notions liées

- [[Activités de transfert]]
- [[Activité 3 - Faire circuler l'information]]
- [[Chapitre 4 - Économie d'énergie et tolérance aux pannes]]
- [[Le fil rouge de l'énergie]]

---
*Activités de transfert. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
