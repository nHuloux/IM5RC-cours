---
title: "Budget énergétique d'un nœud"
chapitre: 4 - Économie d'énergie et tolérance aux pannes
type: concept
tags: [reseaux-de-capteurs, chapitre-4, concept]
---

# Budget énergétique d'un nœud

> **Définition.** Estimation de l'autonomie d'un nœud à partir de la capacité de sa source d'énergie et de sa consommation moyenne : T_vie ≈ C / I_moy.

Un nœud consomme dans quatre activités, très inégalement : la **communication radio** (de loin le premier poste, en émission comme en écoute), la **capture** (variable selon le capteur), le **calcul** (relativement peu coûteux) et les **fuites au repos** (faible mais permanent).

Le courant moyen se calcule en pondérant les courants de chaque état (émission, écoute, mesure, sommeil) par le temps passé dans chacun : I_moy = Σ(Iᵢ·tᵢ) / Σtᵢ.

## Le calcul complet, avec des valeurs de datasheet

Nœud LoRa équipé d'un SX1276, une mesure par minute, pile de 2400 mAh.

| État | Courant | Durée par cycle | Charge |
|---|---|---|---|
| Sommeil profond | 0,005 mA | 59,79 s | 0,299 mA·s |
| Mesure (MCU + capteur) | 5 mA | 100 ms | 0,500 mA·s |
| Émission SF7, 20 octets, +13 dBm | 29 mA | 62 ms | 1,798 mA·s |
| Fenêtres de réception, classe A | 10,8 mA | 50 ms | 0,540 mA·s |
| **Total sur un cycle de 60 s** | | **60 s** | **3,137 mA·s** |

- I_moy = 3,137 / 60 ≈ **0,052 mA**
- T_vie = 2400 mAh / 0,052 mA ≈ 46 000 h ≈ **5,2 ans**
- Rapport cyclique hors sommeil ≈ **0,35 %**

Ce que le tableau montre et que la formule seule ne montre pas : le sommeil occupe 99,65 % du temps mais moins de 10 % de la charge, tandis que la radio occupe 0,18 % du temps et près de 75 % de la charge. Voir le graphique dans [[Duty cycling]].

**Contre-exemple à faire calculer.** Si on laissait la radio en écoute permanente à 10,8 mA, l'autonomie tomberait à 2400 / 10,8 ≈ 222 h, soit **neuf jours** au lieu de cinq ans. Le rapport est de plus de deux cents : voilà pourquoi le duty cycling est vital.

**Variante à faire calculer.** Passer en SF12 pour gagner de la portée allonge le temps d'antenne de 62 ms à environ 1,5 s. La charge d'émission passe de 1,8 à 43,5 mA·s, I_moy à ≈ 0,74 mA, et l'autonomie tombe sous les **quatre mois**. La portée se paie en énergie — la boucle est refermée avec [[Compromis portée-débit-consommation]].

**À retenir.** Le poste dominant est la radio — non seulement en émission, mais aussi en écoute. Une radio allumée « au cas où » vide la batterie aussi sûrement qu'une radio qui émet. Toute la stratégie d'économie d'énergie consiste donc à éteindre la radio le plus souvent possible.

## Notions liées

- [[Unité de communication (transceiver)]]
- [[Unité d'alimentation]]
- [[Duty cycling]]
- [[Compromis portée-débit-consommation]]
- [[Le fil rouge de l'énergie]]

---
*Chapitre 4 — Économie d'énergie et tolérance aux pannes. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
