---
title: "Terrain - Bâtiment intelligent"
chapitre: 6 - Activités de transfert
type: terrain
tags: [reseaux-de-capteurs, activite, terrain]
---

# Terrain - Bâtiment intelligent

> **Le terrain en une phrase.** Un immeuble tertiaire des années 1980 à instrumenter sans percer les murs, où la contrainte n'est pas la distance mais la densité, le béton et les données personnelles.

## Le contexte

Bâtiment tertiaire de 4 200 m², cinq niveaux, environ 300 postes de travail.
Rénovation énergétique en cours : le maître d'ouvrage veut mesurer avant
d'investir, puis piloter. Le bâtiment reste occupé pendant les travaux.

| Zone | Étendue | Particularité |
|---|---|---|
| Plateaux de bureaux | 5 niveaux, ~700 m² chacun | cloisons légères, faux plafonds |
| Circulations et sanitaires | 5 niveaux | noyau béton, cage d'escalier |
| Locaux techniques | sous-sol et toiture | CTA, chaufferie, TGBT |
| Parking et extérieur | sous-sol | dalle béton, aucun signal extérieur |

## Ce qu'il faut observer

- **Qualité d'air et confort** : CO₂, température, humidité par zone de 50 m²,
  soit environ 90 points. Le CO₂ est ce qui pilote la ventilation.
- **Occupation réelle** : présence par bureau et par salle de réunion, pour
  arrêter de chauffer et d'éclairer des locaux vides.
- **Consommations** : sous-comptage électrique par étage et par usage, relevés de
  la chaufferie.
- **Défauts** : température de départ et de retour des circuits, pour repérer un
  équipement qui dérive avant la panne.

## Ce que le terrain impose

- **Environ 350 points de mesure** dans un volume restreint. Le problème est la
  densité et le partage du canal, pas la portée.
- **Du béton armé partout dans le noyau.** Une dalle ou un voile coûte bien plus
  qu'une cloison de bureau : la traversée verticale est le vrai obstacle.
- **Le 2,4 GHz est déjà occupé** par le Wi-Fi de l'entreprise. La cohabitation se
  prépare, elle ne s'improvise pas.
- **Une infrastructure existe déjà** : réseau Ethernet, PoE dans les faux plafonds,
  local technique par étage. Poser une passerelle ne coûte presque rien.
- **La présence est une donnée personnelle.** Savoir qu'un bureau nominatif est
  occupé, c'est savoir qui est là et à quelle heure.
- **La maintenance est contractuelle** : l'exploitant intervient sur signalement,
  et facture chaque déplacement. Un capteur muet doit être détecté sans tournée.

## Points de départ dans le cours

- [[Domaines d'application des WSN]] — le bâtiment intelligent y figure au titre du confort et de la supervision énergétique.
- [[Contraintes des réseaux de capteurs]] — ici, passage à l'échelle et coût unitaire priment.
- [[Thread]] et [[Zigbee]] — les deux familles historiquement dédiées à ce terrain.

## Notions liées

- [[Activités de transfert]]
- [[Topologie maillée (mesh)]]
- [[Couche MAC et accès au canal (CSMA-CA)]]
- [[Sécurité des réseaux de capteurs]]

---
*Activités de transfert. Cours [IM5RC] Réseaux de capteurs, MIRA 3A.*
