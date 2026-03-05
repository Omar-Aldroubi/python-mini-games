# 🎮 Projet POO : Collection de Jeux en Python

Ce projet est une application de bureau regroupant trois simulations et jeux classiques, développée en Python avec l'interface graphique Tkinter. Il a été réalisé dans le cadre de notre projet universitaire de Programmation Orientée Objet (L1 Informatique).

##  L'équipe

* **Omar Aldroubi** : Conception de `PlanetTk` et du jeu de Conway.
* **Moussa Amouri** : Interface principale (`MyApp`) et jeu Snake.
* **Rafik Hamouche** : Conception de `PlanetAlpha` et jeu Turmites.

---

##  Les Jeux Inclus

1. **Snake 🐍** : Le jeu d'arcade classique. Dirigez le serpent, mangez les pommes rouges pour grandir et augmenter votre score, mais évitez les murs, votre propre queue, et les pommes moisies mortelles !
2. **Le Jeu de la Vie (Conway) 🦠** : Un automate cellulaire mythique. Dessinez vos propres motifs de "cellules" sur la grille, lancez la simulation et observez l'évolution de la population selon les lois mathématiques de survie, de naissance et de mort.
3. **Turmites (Fourmi de Langton) 🐜** : Une simulation d'automate cellulaire. Une "fourmi" se déplace sur la grille selon des règles très simples (tourner à droite ou à gauche selon la couleur de la case), créant à terme un motif complexe et infini.

---

##  Architecture Technique
Le projet repose sur une architecture orientée objet pour bien séparer la gestion de la fenêtre, l'affichage graphique et la logique des jeux:
* **`MyApp.py`** : Point d'entrée du programme et gestionnaire du menu principal.
* **`PlanetTk.py`** : Moteur de rendu graphique utilisant le `Canvas` de Tkinter pour dessiner les grilles et les éléments visuels.
* **Pygame / Winsound** : Gestion de la musique de fond multiplateforme.

##  Installation et Lancement

**Prérequis :**
* Python 3 installé sur votre machine.
* La librairie `pygame` (pour l'audio).
