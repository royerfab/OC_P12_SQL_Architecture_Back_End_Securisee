# Projet 12 Développeur d'application Python : Développez une architecture back-end sécurisée avec Python et SQL

## Informations générales

Ce projet constitue un examen dans le cadre du parcours Développeur d'application Python d'OpenClassrooms, il est codé avec le langage Python.
Concrètement, il consiste à créer une base de données avec Python et SQL.

## Auteur

Fabien ROYER

## Contributions

Le projet est achevé depuis février 2024.

## Installation

Création de l'environnement :
```bash
python -m venv env
```

Lancement de l'environnement :
```bash
env\Scripts\activate
```

Utilisez le _package installer_ [pip](https://pypi.org/project/pip/) pour installer les packages inclus dans le fichier 
requirements.txt, pour cela utilisez dans le terminal la commande :

```bash
pip install -r requirements.txt
```

## Création de la base de données

Création de la base de données :

- Installer MySQL sur votre machine.
- Créer une base de données et un utilisateur.
- Aller dans le fichier `config.py`  dans le dossier `models` .
- Mettre à jour les informations de connexion.


## Utilisation

Pour exécuter le code, il faut entrer la commande suivante dans le terminal :

```bash
python main.py
```

Ce programme permet de gérer, par les commandes du terminal, une base de données contenant des utilisateurs, des clients, des contrats et des événements. Les utilisateurs sont répartis en trois équipes et tous peuvent consulter les informations de la base de données. Selon l'équipe dans laquelle ils sont, les utilisateurs peuvent créer ou modifier des clients, des contrats et des événements.

