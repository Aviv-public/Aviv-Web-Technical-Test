# Projet - Carte des prix à Paris

L’objectif est de réaliser une carte des prix moyens (€/m2) de mise en vente par arrondissement à Paris, accompagnée de statistiques, à partir d'une API d'annonces de Meilleurs Agents.
Voici un exemple de ce qu’on veut obtenir au final :

![image 2](pricemap/img/image2.png)
![image 1](pricemap/img/image1.png)

Une partie du projet vous est déjà fourni. Pour le faire fonctionner, les outils suivants sont nécessaires :
- `docker`
- `docker-compose`
- `make`

Pour le reste, utilisez les outils que vous souhaitez.

Ce qui est déjà en place:
- une application web de visualisation (`pricemap`)
- une base de données (`PostgreSQL`)
- une API d'annonces de biens immobilier sur Paris (`listingapi`)
- un premier jet du code pour la partie 1 ("Collecter l'information")

**L'ensemble de votre code doit tourner dans le conteneur `pricemap`.**

Une documentation sur le fonctionnement du projet est disponible [ici](./usages.md) pour savoir comment démarrer le projet, entrer dans un conteneur si besoin...


## 1 - Collecter l’information

On souhaite collecter l'ensemble des annonces de biens immobilier sur Paris. Ces informations seront à récupérer depuis l'API d'annonces fournie (`listingapi`), qu'il faudra parcourir entièrement.

**Il ne faut donc pas modifier `listingapi`, l'API ne sert qu'à servir les données.**

On peut accéder à cette API, une fois le projet démarré :
- depuis la machine locale via : http://localhost:8181/listings/32682
- depuis le conteneur de votre application `pricemap` via: http://listingapi:5000/listings/32682

Afin de commencer, un premier jet du code existe déjà dans le fichier `app.py`. Ce code ajoute un endpoint `/update_data` à l'application `pricemap` qui lance la récupération de la donnée.
**Le code est fonctionnel, mais il existe plusieurs améliorations possibles.**
L'objectif de cette partie est de retravailler et compléter ce code déjà existant, afin de le rendre plus propre et plus proche de l'état de l'art.
Cette partie est libre, il est donc possible de déplacer le code, d'ajouter des bibliothèques, de changer la façon dont le code est appelé, etc.



#### 1.1 -  Filtre par localisation

Au sein de Paris, nous souhaitons sectoriser les annonces par arrondissement.

Lors des appels à `listingsapi`, le paramètre de la requête `place_id` prendra donc successivement pour valeur les identifiants des arrondissements de Paris tels qu’indiqués dans le tableau ci-dessous.

Ces identifiants sont également disponibles en base de données, dans le schéma public dans une table nommée `geo_place`, contenant les arrondissements de Paris et leurs cog (Code Officiel Géographique).

| Arrondissement | Id |
| ------- | ----------|
| Paris 1 | 32682 |
| Paris 2 | 32683 |
| Paris 3 | 32684 |
| Paris 4 | 32685 |
| Paris 5 | 32686 |
| Paris 6 | 32687 |
| Paris 7 | 32688 |
| Paris 8 | 32689 |
| Paris 9 | 32690|
| Paris 10 | 32691 |
| Paris 11 | 32692 |
| Paris 12 | 32693 |
| Paris 13 | 32694 |
| Paris 14 | 32695 |
| Paris 15 | 32696 |
| Paris 16 | 32697 |
| Paris 17 | 32698 |
| Paris 18 | 32699 |
| Paris 19 | 32700 |
| Paris 20 | 32701 |


#### 1.2 - Pagination

L'API `listingsapi` renvoie des pages de 20 annonces. Il vous faudra donc parcourir toutes les pages pour tous les arrondissements, via la paramètre `?page=<numero_de_page>`.

Exemple: http://listingapi:5000/listings/32682?page=7

Le nombre de pages de résultat est différent pour chaque arrondissement : de zéro à plusieurs dizaines de pages. Il faudra imaginer un mécanisme s’adaptant au nombre de pages à parcourir. Il y a plusieurs manières de faire.

### 1.3 Extraction des caractéristiques des annonces

Pour chaque annonce, on est intéressé par les caractéristiques suivantes :
- `listing_id` : identifiant de l’annonce pour MeilleursAgents
- `place_id` : identifiant de l’arrondissement (celui passé en paramètre de la recherche)
- `price` : prix de mise en vente, en valeur entière d’euros
- `area` : superficie du bien, en valeur entière de mètres carrés
- `room_count` : nombre de pièces du bien, en valeur entière également ;

Il se peut que les caractéristiques ne soient pas exposées comme souhaité par l'API `listingsapi`, mais que certaines d'entre elles soient à extraire. Attention aux appartements de 1 pièce qui sont notés « Studio »

### 1.4 - Structure des informations en base de données

Une fois les annonces extraites en respectant les caractéristiques ci-dessus, elles doivent être ensuite stockées en base de données dans une ou plusieurs tables qui faudra définir au préalable.
En plus de leurs caractéristiques, on veut aussi modéliser l’évolution des annonces dans le temps. Plus concrètement, on veut connaître :

- la date de mise en ligne (ou au moins la date à laquelle on l’a vue pour la première fois)
- la date de retrait du site (ou au moins la dernière date à laquelle on l’a vue)
- l’historique complet des prix.

Voici les informations requises pour se connecter au serveur de base de données :

- type : PostgreSQL (module `psycopg2` en Python)
- host : `db`
- port: `5432`
- user : `pricemap`
- password : `pricemap`
- database : `pricemap`

## 2 - Restituer l’information

La carte et l’histogramme présentés en introduction de ce document sont servis par une application web écrite en Python à l’aide du micro-framework Flask.

Comme pour la partie 1, l’application web est déjà fonctionnelle mais peut être améliorée.

### 2.1 - Cartographier les prix par arrondissement

Au chargement de la page web, le code JavaScript en charge de la génération de la carte interroge l’application web Python afin d’obtenir la liste des entités géographiques à afficher. L’application web fournit en retour une structure de données au format GeoJSON contenant la liste des arrondissements à afficher, leur forme géométrique ainsi qu’un prix moyen, définit aléatoirement pour le moment. La couleur de la forme géométrique dépend du prix de l’arrondissement qu’elle représente, selon la même échelle de couleurs que celle actuellement utilisée pour la carte de Paris sur le site web de MeilleursAgents.

Pour chaque arrondissement, le prix moyen par mètre carré réel est calculé pour être ensuite affiché sur le site web.

Le code est dans l'endpoint `/geoms` dans `pricemap/pricemap/blueprints/api.py`. Comme pour la première partie, le code est fonctionnel mais peut être amélioré : requête, calcul de la donnée, schémas de stockage de la donnée, etc.

### 2.2 - Afficher des statistiques par arrondissement

Lorsque l’on clique sur un arrondissement, un histogramme apparaît. Cet histogramme représente la distribution du volume d’annonces par gamme de prix dans cet arrondissement. De la même manière que précédemment, le code JavaScript en charge de la génération de cet histogramme interroge l’application web avant chaque affichage, en passant le code de l’arrondissement en paramètre. L’application web fournit en retour une structure de données au format JSON contenant, entre autres, les valeurs de chacune des barres de l’histogramme. L’axe des ordonnées est alors mis à l’échelle automatiquement en fonction des valeurs fournies.

Pour l’arrondissement ciblé, la distribution des annonces par gamme de prix est calculée côté API pour être ensuite intégrée à la réponse de l’application web. Le code JavaScript va utiliser cette réponse pour générer l’histogramme.

Le code est dans l'endpoint `/get_price/<path:cog>` dans `pricemap/pricemap/blueprints/api.py`. Comme pour l'autre endpoint, le code peut être aussi amélioré.
Vous pouvez changer la distribution, les labels, la méthode de calcul,etc. de l'histogramme.

### 2.3 - Afficher le prix moyen de l’arrondissement (bonus)

Entre la carte et l’histogramme, nous n’affichons nulle part le prix moyen de l’arrondissement de manière numérique. Que faut-il faire pour l’afficher sur la page web lorsqu’on clique sur un arrondissement de la carte ?

## 3 - Industrialisation

### 3.1 - Passage à l'échelle

On souhaite maintenant avoir l'historique des prix à l'échelle de la France pour offrir une carte des prix contenant des valeurs les plus fraîches possibles aux utilisateurs de notre site grand public.

Pour cela vous devez réfléchir à une architecture qui respectera les contraintes suivantes:

1. insérer les prix des annonces sur toute la France en moins de 5 minutes.

2. assurer un temps de réponse inférieur à 500ms lors de la consultation de la carte quel que soit le nombre d'utilisateurs connectés simultanément.

Vous avez carte blanche en terme d'infrastructure, aucune limitation de budget, de langage ou de technologie, ni aucune autre contrainte.

On souhaite avoir comme rendu un schéma (par exemple sur https://draw.io/) qui servira de base de discussion en debrief de test.

