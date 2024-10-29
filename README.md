# Web_Scraping
# Projet de Web Scraping des Annonces de Voitures

Ce projet consiste à extraire des informations sur les voitures d'occasion à partir du site [Wandaloo](https://www.wandaloo.com). Les données sont enregistrées dans un fichier CSV pour une analyse ultérieure.

## Fonctionnalités

- Extraction des informations suivantes pour chaque voiture :
  - Nom
  - Prix
  - Carburant
  - Modèle
  - CV (puissance fiscale)
  - KM (kilométrage)
  - Ville

- Support pour le scraping de plusieurs pages d'annonces.

## Prérequis

Avant de commencer, assurez-vous d'avoir Python installé sur votre machine. Vous aurez également besoin des bibliothèques suivantes :

- `requests`
- `beautifulsoup4`
- `csv`

Vous pouvez installer les bibliothèques requises avec la commande suivante :

```bash
pip install requests beautifulsoup4
