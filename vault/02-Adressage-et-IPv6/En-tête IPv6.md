---
title: "En-tête IPv6"
chapitre: 2 - Adressage et protocole IPv6
type: concept
tags: [reseaux-de-capteurs, chapitre-2, concept]
---

# En-tête IPv6

> **Définition.** En-tête simplifié par rapport à IPv4, de 40 octets de taille fixe, pour accélérer le traitement par les routeurs.

Il contient notamment : la version, une classe de trafic (priorité), un *flow label*, la longueur des données utiles, le champ *Next Header* (protocole de niveau supérieur ou extension), le champ *Hop Limit* (équivalent du TTL d'IPv4), et les adresses source et destination sur 128 bits chacune. Les fonctions optionnelles sont reportées dans des en-têtes d'extension chaînés plutôt que dans un en-tête de taille variable. C'est ce poids fixe de 40 octets qui pose problème face à une trame IEEE 802.15.4 de 127 octets — d'où la compression d'en-tête de 6LoWPAN.

## Repères chiffrés

| | IPv6 | IPv4 |
|---|---|---|
| Taille | 40 octets, **fixe** | 20 à 60 octets, variable |
| Nombre de champs | 8 | 12 champs fixes + champ Options |
| Somme de contrôle d'en-tête | supprimée | présente, à recalculer à chaque saut |
| Fragmentation par les routeurs | interdite (reportée sur la source) | autorisée |
| Options | en-têtes d'extension chaînés | dans l'en-tête lui-même |

**À retenir.** Le gain de traitement vient moins de la taille que du caractère **fixe** de l'en-tête : un routeur sait à l'avance où lire chaque champ, n'a pas de somme de contrôle à recalculer et n'a pas à fragmenter. Mais pour un lien de 127 octets, ces 40 octets fixes restent un coût net — c'est exactement la tension que résout [[6LoWPAN]].

## Notions liées

- [[IPv6]]
- [[6LoWPAN]]
- [[IPv4 et pénurie d'adresses]]

---
*Chapitre 2 — Adressage et protocole IPv6. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
