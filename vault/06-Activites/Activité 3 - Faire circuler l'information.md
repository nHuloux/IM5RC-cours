---
title: "Activité 3 - Faire circuler l'information"
chapitre: 6 - Activités de transfert
type: activite
tags: [reseaux-de-capteurs, activite, chapitre-2, chapitre-3]
---

# Activité 3 - Faire circuler l'information

> **En une phrase.** Compter les octets d'une trame réelle, nommer les machines, et choisir comment le paquet trouve son chemin.

**Durée indicative** : 3 h, en binôme.
**Prérequis** : la technologie retenue en
[[Activité 2 - Choisir une technologie radio sous contrainte]].
**Appui** : [[Chapitre 2 - Adressage et protocole IPv6]] et la partie routage du
[[Chapitre 3 - La communication dans les réseaux de capteurs]].

## Ce que vous devez savoir faire à la fin

- Établir le budget d'octets d'une trame et dire ce qu'il reste pour les données.
- Poser un plan d'adressage et justifier le mode d'attribution.
- Choisir une famille de routage à partir de la dynamique de votre terrain, et non par habitude.

## 1. Parcours de notions

**Adressage** — pourquoi IPv6 jusqu'au capteur, et à quel prix :

| Note | La question à vous poser |
|---|---|
| [[Pile protocolaire de l'IoT contraint]] | Placez votre terrain sur cette pile, couche par couche. |
| [[IPv4 et pénurie d'adresses]] · [[IPv6]] | Combien d'adresses votre terrain consomme-t-il aujourd'hui, et dans dix ans ? |
| [[Structure d'une adresse IPv6]] · [[Types d'adresses IPv6]] | Pourquoi la disparition du broadcast est-elle une **mesure d'économie d'énergie** ? |
| [[SLAAC]] · [[DHCPv6]] · [[NDP (Neighbor Discovery Protocol)]] | Avec ou sans état : lequel convient à un parc que personne ne configure nœud par nœud ? |
| [[6LoWPAN]] · [[En-tête IPv6]] | La compression IPHC n'est pas une élégance protocolaire. Qu'est-ce qu'elle achète, concrètement ? |
| [[CoAP]] | Pourquoi pas HTTP ? |

**Routage** — comment le paquet trouve son chemin :

| Note | La question à vous poser |
|---|---|
| [[Routage dans les réseaux ad-hoc]] · [[Réseau ad-hoc (MANET)]] | Votre terrain est-il seulement un réseau ad-hoc ? |
| [[Protocoles proactifs (OLSR)]] · [[Protocoles réactifs (AODV)]] · [[Protocoles hybrides (ZRP)]] | Trois façons de payer : en permanence, à la demande, ou les deux. Laquelle correspond au trafic de votre terrain ? |
| [[RPL]] | Le trafic de votre terrain est-il bien celui pour lequel RPL est conçu ? |
| [[Qualité de lien (PRR, ETX, RSSI, LQI)]] | Pourquoi le nombre de sauts est un mauvais critère — et ce que cela change à un placement de nœud. |

## 2. Transfert sur le terrain

### 2.1 Le budget d'octets d'une de vos trames

Prenez **un** message réel de votre tableau des grandeurs et refaites, avec vos
chiffres, le tableau de [[6LoWPAN]] :

| Poste | Sans compression | Avec 6LoWPAN |
|---|---|---|
| Trame PHY | | |
| En-tête MAC + FCS | | |
| En-tête réseau | | |
| En-tête transport | | |
| **Données applicatives disponibles** | | |

Puis répondez : **combien de mesures tiennent dans une trame ?** Et si vous
activez la sécurité, sachant qu'elle coûte de l'ordre de 21 octets
([[Sécurité des réseaux de capteurs]]) ?

Si votre terrain est en LoRaWAN, le tableau n'est pas celui-là : la taille utile
dépend du facteur d'étalement. Établissez le vôtre à partir de
[[LoRa et LoRaWAN]], et la conclusion sera du même ordre — il reste peu de place.

### 2.2 Le plan d'adressage

Combien de sous-réseaux, quel préfixe par zone, quelle méthode d'attribution
([[SLAAC]] ou [[DHCPv6]]), et quels groupes multicast pour les commandes
descendantes. Justifiez la méthode par la contrainte d'exploitation de votre
terrain, pas par la facilité.

### 2.3 Le choix de routage

Si votre architecture est en étoile, dites-le et expliquez **pourquoi il n'y a pas
de routage** — c'est une réponse complète, à condition d'être argumentée.

Si elle est maillée, choisissez une famille et justifiez-la par la **dynamique**
de votre terrain : à quelle fréquence la topologie change-t-elle réellement ?

- **Viticole** — topologie quasi statique, trafic essentiellement montant, nœuds
  sur pile. Regardez ce que le timer Trickle de [[RPL]] fait dans ce régime.
- **Bâtiment** — beaucoup de nœuds, liens stables mais portes qui s'ouvrent et se
  ferment, et un vrai besoin de trafic descendant vers les actionneurs. Le mode de
  fonctionnement de RPL n'est pas indifférent.
- **Industriel** — chariots en mouvement, liens qui se dégradent quand une machine
  bouge. C'est le terrain où la question proactif / réactif se pose vraiment ;
  regardez aussi [[TSCH]], et dites ce qu'il apporte et ce qu'il impose.

### 2.4 L'arithmétique de l'ETX

Sur votre plan, choisissez un nœud éloigné et deux chemins possibles vers la
passerelle. Affectez un ETX plausible à chaque lien, additionnez, et montrez le
cas où **le chemin le plus long en nombre de sauts est le meilleur**. Concluez sur
ce que cela impose au placement de vos nœuds relais.

## 3. Livrable

Le budget d'octets chiffré, le plan d'adressage, le choix de routage argumenté par
la dynamique du terrain, et le calcul d'ETX sur deux chemins.

## Critères de réussite

- Le nombre de mesures par trame est un **chiffre**, obtenu par soustraction.
- Le choix SLAAC / DHCPv6 est justifié par l'exploitation.
- Le choix de routage s'appuie sur la dynamique observée, pas sur la popularité du protocole.
- Le calcul d'ETX débouche sur une conséquence pratique de placement.

## Pièges fréquents

- Traiter l'adressage comme une formalité administrative : ici, chaque octet
  d'en-tête est un octet de donnée en moins et de l'énergie en plus.
- Choisir RPL parce que c'est le protocole du cours, sans vérifier que le profil de
  trafic correspond.
- Oublier que la sécurité et la compression se disputent la même trame.

## Notions liées

- [[Activités de transfert]]
- [[Activité 2 - Choisir une technologie radio sous contrainte]]
- [[Activité 4 - Tenir dans la durée]]
- [[Chapitre 2 - Adressage et protocole IPv6]]

---
*Activités de transfert. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
