---
title: "Passerelle (gateway)"
chapitre: 1 - Introduction, architectures et applications
type: concept
tags: [reseaux-de-capteurs, chapitre-1, concept]
---

# Passerelle (gateway)

> **Définition.** Nœud particulier (sink/gateway) disposant de plus de ressources (alimentation secteur, liaison Internet, IP publique), qui fait le pont entre le réseau de capteurs et une infrastructure classique.

Les nœuds ne dialoguent en général pas directement avec l'utilisateur : l'information remonte vers la passerelle, qui la relaie vers Internet, un serveur cloud, une base de données ou un tableau de bord. La passerelle est un point critique du réseau : si elle tombe, tout le réseau devient aveugle, d'où l'intérêt d'une redondance de passerelle pour les systèmes critiques.

## Notions liées

- [[Réseau de capteurs sans fil (WSN)]]
- [[Topologie en étoile]]
- [[Mécanismes de résilience]]
- [[RPL]]

---
*Chapitre 1 — Introduction, architectures et applications. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
