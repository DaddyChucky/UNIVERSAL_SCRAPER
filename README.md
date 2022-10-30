# UNIVERSAL_SCRAPER

## [EN] Description:
- Generic web crawler/scraper for any website.
- By simply giving a starting link, program will reconstruct a link hierarchy, and travel each and every one of them while outputing page's data iteratively.
- Breadth-First Search (BFS) algorithm is currently implemented. Will add Depth-First Search (DFS) soon after BFS is done with its proof of concept. Update: BFS satisfies the POC, no need to do DFS implementation. Feel free to contribute.
- You can let the script run, and all the data retrieved can be collected in the OUT/data.json as a JSON dictionary (key as the URI).
- Once the data collection is completed, you can run the purgatory file to cleanup all of your dictionaries collected. This is crucial, and especially resourceful for NLP data modeling, or any modeling for future usage.

## [FR] Description:
- Robot d'exploration d'un site Web quelconque.
- Avec qu'un seul lien de départ, le programme reconsruira une hiérarchie de liens et parcourra chacun d'eux tout en produisant les données des pages de manière itérative.
- L'algorithme de parcours en largeur (BFS) est actuellement implémenté. Je prévois ajouter l'algorithme de parcours en profondeur (DFS) peu de temps après que BFS aura terminé sa preuve de concept. Mise à jour: l'algorithme BFS remplit les satisfactions du POC; nul besoin d'implémenter un DFS. Vous êtes libre de contribuer au repo.
- Vous pouvez laisser le script s'exécuter et toutes les données récupérées peuvent être collectées dans le OUT/data.jsons sous forme de dictionnaire JSON (dont la clé est l'URI).
- Une fois la collecte de données terminée, vous pouvez exécuter le fichier purgatoire pour nettoyer tous vos dictionnaires collectés. Ceci est une étape cruciale pour une modélisation NLP future, ou toute autre modélisation post-mortem.

## Author / Auteur:
- Charles De Lafontaine
