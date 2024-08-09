
---

# Django Introduction Project

## Description

Ce projet a pour but d'introduire Django aux étudiants en démontrant la puissance de ce framework. Il met en évidence plusieurs fonctionnalités essentielles qui permettent de créer rapidement des applications web robustes. Plus précisément, ce projet couvre :

- **Gestion des paginations** : Django offre des outils puissants pour gérer les paginations de manière efficace.
- **Authentification** : Utilisation de classes spécifiques pour gérer l'authentification des utilisateurs.
- **Class-Based Views (CBV)** : Introduction aux vues basées sur des classes pour une organisation et une réutilisation du code plus efficace.
- **Function-Based Views (FBV)** : Utilisation des vues basées sur des fonctions pour une approche plus directe dans la gestion des requêtes.

## Fonctionnalités

1. **Gestion des Auteurs et Livres** :
   - Ajouter, modifier, supprimer, et afficher les auteurs et les livres dans une base de données.
   - Pagination automatique pour l'affichage des listes d'auteurs et de livres.

2. **Authentification des Utilisateurs** :
   - Système d'authentification intégré avec gestion des sessions.
   - Accès restreint à certaines pages en fonction de l'état de connexion de l'utilisateur.

3. **Vues Basées sur des Classes (CBV)** :
   - Utilisation des CBV pour organiser les vues de manière structurée et modulaire.

4. **Vues Basées sur des Fonctions (FBV)** :
   - Exemple d'implémentation de FBV pour les opérations CRUD simples.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- Python 3.x
- Django 5.x
- Un environnement virtuel (recommandé)

## Installation

1. Clonez ce dépôt sur votre machine locale :
   ```bash
   git clone https://github.com/soszaboss/django_presentation.git
   cd django_presentation
   ```

2. Créez et activez un environnement virtuel :
   ```bash
   python -m venv env
   source env/bin/activate  # Sur Windows, utilisez `env\Scripts\activate`
   ```

3. Installez les dépendances requises :
   ```bash
   pip install -r requirements.txt
   ```

4. Appliquez les migrations de la base de données :
   ```bash
   python manage.py migrate
   ```

5. Créez un superutilisateur pour accéder à l'admin de Django :
   ```bash
   python manage.py createsuperuser
   ```

6. Lancez le serveur de développement :
   ```bash
   python manage.py runserver
   ```

7. Accédez à l'application dans votre navigateur à l'adresse suivante :
   ```
   http://127.0.0.1:8000/
   ```

## Utilisation

- **Gestion des Auteurs et Livres** :
  - Naviguez vers `/book-management/authors/` pour gérer les auteurs.
  - Naviguez vers `/book-management/books/` pour gérer les livres.

- **Formulaires** :
  - Les formulaires sont gérés via des classes (`forms.py`) qui permettent de définir facilement les champs et la validation.

## Structure du Projet

- `models.py` : Définit les modèles pour les auteurs et les livres.
- `views.py` : Contient les vues basées sur les classes et les fonctions pour gérer les auteurs et les livres.
- `forms.py` : Contient les classes de formulaires pour gérer la saisie utilisateur.
- `urls.py` : Gère les routes de l'application.
- `templates/` : Contient les fichiers HTML pour le rendu des pages.
