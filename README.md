# TP1-AUT23-BIBLIO


# Bibliothèque Python

Ce projet représente une application de gestion de bibliothèque en utilisant Python. Il permet d'ajouter des adhérents, des livres, d'effectuer des emprunts, de retourner des livres, etc.

## Fonctionnalités

- Ajouter et supprimer des adhérents.
- Ajouter et supprimer des livres.
- Effectuer des emprunts.
- Retourner des livres et mettre à jour l'état des emprunts.
- Afficher la liste des adhérents, des livres, des emprunts, etc.

## Structure du Code

Le code est divisé en plusieurs classes :

- `Personne`: Représente une personne avec un nom, prénom et âge.
- `Adherent`: Hérite de `Personne` et ajoute un numéro d'adhérent.
- `Document`: Représente un document avec un titre, un nombre de pages et un ISBN.
- `Livre`: Hérite de `Document` et ajoute des informations spécifiques à un livre.
- `Emprunt`: Représente un emprunt avec un adhérent, un livre, une date d'emprunt et une date de retour.
- `Bibliotheque`: Gère les adhérents, les livres et les emprunts, avec des méthodes pour ajouter, supprimer et afficher ces éléments.
- `InterfaceUtilisateur`: Fournit un menu interactif pour interagir avec la bibliothèque.

## Utilisation

1. Exécutez le fichier `main.py` pour lancer l'interface utilisateur.
2. Suivez les instructions du menu pour effectuer des actions telles que l'ajout d'adhérents, de livres, etc.

## Sauvegarde des Données

Les adhérents et les livres sont sauvegardés dans des fichiers JSON (`adherents.json` et `livres.json`) pour assurer la persistance des données entre les sessions.

## Dépendances

Ce projet utilise la bibliothèque standard de Python et ne nécessite aucune dépendance externe.

---

**Note:** Assurez-vous d'avoir Python installé sur votre machine pour exécuter ce programme.

