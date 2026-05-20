# KNN-oriente
# Projet KNN - Programmation Orientée Objet (Full Vanilla)

Ce projet implémente l'algorithme des **K-Plus Proches Voisins (KNN)** en Python sans utiliser de bibliothèques externes de Machine Learning (comme `scikit-learn` ou `numpy`). Le code est entièrement structuré selon le paradigme de la **Programmation Orientée Objet (POO)**.

## 📁 Structure du Projet

Le projet est découpé en plusieurs modules indépendants (une classe par fichier) pour respecter les principes de modularité et faciliter le versionnage avec Git :

* **`knn.py`** : Contient la classe `KNN` principale avec les méthodes `fit` (mémorisation), `distance` (calcul de la distance euclidienne) et `predict` (vote majoritaire).
* **`evaluator.py`** : Contient la classe `Evaluator` dédiée au calcul des métriques de performance, notamment l'**Accuracy** (taux de bonnes réponses).
* **`gridsearch.py`** : Contient la classe `GridSearch` qui permet de tester une liste de valeurs pour l'hyperparamètre $k$ afin de trouver automatiquement le modèle le plus performant.

## 🚀 Fonctionnalités implémentées

- [x] **Attributs d'instance** pour stocker les paramètres et les données d'entraînement.
- [x] Méthode **`fit`** pour l'apprentissage paresseux (*lazy learning*).
- [x] Méthode **`predict`** (gestion d'un point ou d'une liste de points).
- [x] Calcul de la **distance euclidienne** en Python pur.
- [x] Gestion des **votes majoritaires** via un dictionnaire.
- [x] Métrique d'**évaluation** personnalisée.
- [x] Optimisation des hyperparamètres par **Grid Search**.

## 💻 Comment lancer les tests ?

Chaque fichier contient sa propre zone de test (`if __name__ == "__main__"`). Tu peux les exécuter un par un dans le terminal :

1. Tester le modèle KNN :
```bash
python knn.py