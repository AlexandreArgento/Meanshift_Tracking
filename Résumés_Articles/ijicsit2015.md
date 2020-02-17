### Etapes de l'algorithme
- Sélection de l'objet à tracker à l'initialisation : taille de l'objet (fenêtre), position.
- Estimation de la position moyenne de l'objet dans la fenêtre de recherche.
- Repositionnement de la fenêtre pour que son centre et celui de l'objet coïncident.
- Retour à la deuxième étape jusqu'à-ce que le calcul du centre converge.
- Retour à la deuxième étape pour la "frame" suivante.

### Performances
- Centre de la fenêtre: amélioration de la précision avec une estimation de la direction de déploacement
=> Problème: solution gourmande en temps CPU

### Limites
- Rapidité trop grande de l'objet telle que l'objet, d'une frame à lautre soit situé dans des zones rectangulaires qui ne se recouvrent pas.
=> Solution: combiner l'algorithme avec un filtrage de Kalman ou particulaire.

### Remarques
Aucun détail concernant la méthode d'estimation du centre de l'objet.
L'article mentionne simplement qu'elle repose sur l'histogramme des couleurs à partir de la région sélectionnée.
