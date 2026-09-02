---
title: "Sécurité des réseaux de capteurs"
chapitre: Compléments hors support
type: concept
tags: [reseaux-de-capteurs, complement, concept, securite]
---

# Sécurité des réseaux de capteurs

> **Définition.** Ensemble des mécanismes qui garantissent la confidentialité, l'intégrité, l'authenticité et la disponibilité des données d'un WSN, sous la contrainte que chaque octet et chaque microampère comptent.

Un WSN cumule les facteurs de risque : les nœuds sont **physiquement accessibles** (un capteur dans un vignoble se démonte à la pince), le médium radio est **écoutable et brouillable par nature**, et les ressources sont trop faibles pour la cryptographie asymétrique classique. La sécurité y est donc un problème de dimensionnement autant que de cryptographie.

## Le coût de la sécurité, en octets

C'est la particularité du domaine : le chiffrement ne coûte presque rien en calcul — AES est accéléré en matériel sur la quasi-totalité des transceivers modernes — mais il coûte cher en **place dans la trame**.

| Poste | Coût |
|---|---|
| En-tête auxiliaire de sécurité 802.15.4 | 5 à 14 octets (contrôle, compteur de trames, identifiant de clé) |
| MIC (code d'intégrité) | 4, 8 ou 16 octets |
| **Surcoût courant** | **21 octets** sur les 127 de la trame |
| Surcoût maximal | 30 octets |

Sur une trame de 127 octets, activer la sécurité consomme donc environ un sixième du budget. À croiser directement avec le tableau de [[6LoWPAN]] : c'est ce qui fait passer les données applicatives de 91 à 70 octets, et de 54 à 33 octets sans compression. **La sécurité et la compression d'en-tête ne sont pas deux sujets séparés : elles se disputent la même trame.**

## Ce que fait IEEE 802.15.4

La sécurité est assurée au niveau MAC par **AES-CCM\*** avec une clé AES-128, selon huit niveaux de sécurité configurables :

| Niveau | Chiffrement | Authentification |
|---|---|---|
| 0x00 | non | non |
| 0x01 à 0x03 | non | MIC de 32, 64 ou 128 bits |
| 0x04 | oui (CTR) | non |
| 0x05 à 0x07 | oui | MIC de 32, 64 ou 128 bits |

La protection contre le **rejeu** repose sur un compteur de trames monotone de 4 octets : un paquet dont le compteur est inférieur ou égal au dernier reçu est rejeté.

## Ce que fait LoRaWAN

Deux clés de session, ce qui donne une propriété importante : l'opérateur du réseau vérifie l'intégrité sans pouvoir lire les données.

| Clé (LoRaWAN 1.0.x) | Rôle |
|---|---|
| **NwkSKey** | intégrité et authenticité du message au niveau réseau |
| **AppSKey** | chiffrement de la charge utile, de bout en bout jusqu'au serveur applicatif |

Les deux sont dérivées de l'**AppKey** racine lors du *join* OTAA, ou préprogrammées en ABP — mode plus simple mais nettement moins sûr, puisque les clés de session ne changent jamais. LoRaWAN 1.1 sépare les racines (NwkKey et AppKey) et introduit trois clés réseau distinctes (FNwkSIntKey, SNwkSIntKey, NwkSEncKey).

Anti-rejeu : **DevNonce** côté terminal et **JoinNonce** côté serveur pour la procédure de join, compteurs **FCntUp** et **FCntDown** pour les messages de données.

## Les attaques à connaître

**Génériques aux WSN :**
- **Brouillage** (*jamming*) — saturer le canal. Peu élégant, très efficace, indétectable par la cryptographie.
- **Rejeu** — réémettre un message valide capté plus tôt. Contré par les compteurs de trames.
- **Capture physique / nœud compromis** — récupérer un nœud, en extraire les clés, le reprogrammer. C'est l'attaque la plus spécifique au domaine, et celle contre laquelle la résilience classique ne protège pas : le nœud reste vivant aux yeux du réseau.
- **Sybil** — un nœud se présente sous plusieurs identités pour peser plus lourd dans un vote ou une agrégation.
- **Wormhole** — deux attaquants reliés par un lien rapide créent un raccourci artificiel et attirent le trafic.
- **Selective forwarding** — un relais compromis transmet la plupart des paquets et jette silencieusement ceux qui le dérangent (par exemple les alarmes).
- **Denial of sleep** — attaque proprement énergétique : maintenir la radio du nœud éveillée pour vider sa pile. Le nœud n'est jamais compromis, seulement épuisé. Elle vise exactement ce que le [[Duty cycling]] cherche à protéger.

**Spécifiques à [[RPL]] :**
- **Sinkhole** — un nœud annonce un rank artificiellement bas pour attirer tout le trafic du sous-arbre.
- **Version number attack** — incrémenter le numéro de version du DODAG force une reconstruction complète de l'arbre, à répétition : coût énergétique massif.
- **Rank attack** — manipuler son rank pour dégrader les routes.
- **DAO insider attack** — injecter de faux DAO pour polluer les routes descendantes.

RPL définit trois modes de sécurité (*unsecured*, *preinstalled*, *authenticated*), mais le mode authentifié n'a pas de mécanisme de gestion de clés spécifié, et ces modes sont rarement implémentés dans les piles courantes.

## Sécuriser la couche application

- **DTLS** — TLS adapté à UDP. DTLS 1.2 : RFC 6347 ; DTLS 1.3 : RFC 9147. CoAP sur DTLS s'appelle *coaps* et écoute sur le port **5684**.
- **OSCORE** — RFC 8613, *Object Security for Constrained RESTful Environments*. Protège le message lui-même plutôt que le canal, ce qui lui permet de **traverser les proxies** : indispensable dès qu'une passerelle traduit CoAP en HTTP, là où DTLS s'arrête.

## À retenir

Trois idées à emporter :
1. Le coût de la sécurité dans un WSN n'est pas le calcul, c'est **la place dans la trame et l'énergie de la transmettre**.
2. Le chiffrement ne protège ni du brouillage ni du *denial of sleep* : la **disponibilité** se traite par la redondance, pas par la cryptographie.
3. Un nœud physiquement accessible doit être considéré comme potentiellement compromis. Le vrai travail est alors la **gestion des clés** — clé par nœud plutôt que clé de réseau unique, et capacité à révoquer.

## Notions liées

- [[6LoWPAN]]
- [[IEEE 802.15.4]]
- [[LoRa et LoRaWAN]]
- [[RPL]]
- [[CoAP]]
- [[Mécanismes de résilience]]
- [[Duty cycling]]
- [[Contraintes des réseaux de capteurs]]

---
*Complément hors support. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
