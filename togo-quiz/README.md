# TOGO QUIZ : Application Interactive de Terminal en Python

#### Video Demo: https://youtu.be/YfqONHZwNgE

#### Description:

Togo Quiz est une application interactive en ligne de commande (CLI) développée en Python dans le cadre du projet final du cours CS50P. Ce projet a pour objectif de tester et d'enrichir les connaissances culturelles, historiques, géographiques, politiques et sportives sur le Togo à travers un quiz dynamique, chronométré et esthétiquement soigné dans le terminal.

L'application s'articule autour de plusieurs fonctionnalités clés :

* **Un affichage visuel attrayant** : Au démarrage, le titre du jeu "BIENVENUE SUR TOGO QUIZ" s'affiche dynamiquement en ASCII Art grâce à la bibliothèque `pyfiglet`.
* **Une base de données JSON** : Toutes les questions, options et réponses sont stockées de manière structurée dans un fichier externe `quiz.json`, ce qui permet d'ajouter ou de modifier facilement des questions sans toucher au code source.
* **Un menu de catégories dynamique** : Le programme lit automatiquement les catégories disponibles dans le fichier JSON et propose un menu interactif à l'utilisateur (Histoire, Politique, Géographie, Culture et Traditions, Sport).
* **Un système de chronométrage** : Pour chaque question posée, le programme mesure précisément le temps de réflexion de l'utilisateur à l'aide du module natif `time`.
* **Une mise en forme en tableau** : Les options de réponse de chaque question sont présentées proprement sous forme de grille esthétique grâce à la bibliothèque `tabulate`.
* **Un calcul de score final** : À la fin du quiz, un récapitulatif affiche le score total obtenu sur le nombre de questions de la catégorie.

---

### Structure des Fichiers

Le projet est composé des fichiers suivants, chacun ayant un rôle bien précis :

1. **`project.py`** : C'est le fichier principal du programme. Il contient la logique globale du jeu, la fonction `main()`, le chargement du fichier JSON, la gestion du menu utilisateur, l'affichage des questions avec le chronomètre, ainsi que la fonction `check_answer()` dédiée à la validation des réponses.
2. **`quiz.json`** : C'est le fichier de données (la base de données). Il est structuré sous forme de dictionnaire Python/JSON où chaque clé correspond à une catégorie (ex: `"Histoire"`, `"Politique"`) et contient une liste de dictionnaires regroupant la question, les options de choix et la réponse attendue.
3. **`test_project.py`** : C'est le fichier de tests unitaires exigé par CS50P. Il utilise la bibliothèque `pytest` pour vérifier automatiquement le bon fonctionnement des fonctions pures du projet (`get_only_available_categories`, `check_answer` et `load_quiz_questions`).

---

### Choix de Conception et Justifications

Durant le développement de ce projet, plusieurs choix de conception ont été faits pour répondre aux contraintes du cours CS50P tout en garantissant un code propre et maintenable :

* **Séparation de la logique de vérification (`check_answer`)** : Initialement, la vérification de la saisie utilisateur était imbriquée directement dans la boucle d'affichage des questions. Pour rendre le code plus modulaire et surtout permettre d'écrire des tests unitaires simples avec `pytest` sans avoir à simuler des saisies clavier complexes (`input`), j'ai isolé la comparaison dans une fonction indépendante `check_answer()`.
* **Gestion dynamique des catégories** : Plutôt que de coder en dur les choix de catégories dans le menu, le programme utilise `data.keys()` pour extraire automatiquement les thèmes disponibles depuis le fichier JSON. Cela rend l'application évolutive : si l'on ajoute une nouvelle catégorie dans le fichier JSON, le menu s'adapte tout seul sans modification de `project.py`.
* **Utilisation de bibliothèques externes légères** : L'utilisation de `pyfiglet` apporte une touche visuelle professionnelle dès l'ouverture du terminal, tandis que `tabulate` structure clairement les options pour éviter un affichage brut en texte linéaire difficile à lire.