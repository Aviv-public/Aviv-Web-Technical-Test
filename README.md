# Projet - Carte des prix à Paris 

L’objectif est de réaliser une carte des prix moyens (€/m2) de mise en vente par arrondissement à Paris, accompagnée de statistiques, à partir des annonces diffusées par les agences immobilières sur le site web de MeilleursAgents. 

Voici un exemple de ce qu’on veut obtenir au final : 

![image 2](pricemap/img/image2.png)
![image 1](pricemap/img/image1.png)

## 1 - Collecter l’information 

Sur le site web de MeilleursAgents, dans la rubrique « Acheter », on trouve des annonces de biens immobiliers actuellement proposés à la vente par les agences partenaires de MeilleursAgents. On souhaite collecter cette information.

### 1.1 - Scénario de navigation 

La première étape consiste parcourir l’ensemble des annonces disponibles sur le site web. Elles sont accessibles via une adresse de recherche de la forme suivante : 
`https://www.meilleursagents.com/annonces/achat/search/?transaction_types=TRANSACTION_TYPE.SELL&plac e_ids=32682%2C32684&item_types=ITEM_TYPE.APARTMENT&page=1 `

#### 1.1.1 - Filtre par type de bien 

S’agissant d’une carte à Paris, où les maisons sont suffisamment rares pour être ignorées, nous nous limiterons aux seuls appartements. L’argument item_types sera donc toujours fixé à la valeur `ITEM_TYPE.APARTMENT` 

#### 1.1.2 -  Filtre par localisation 

Au sein de Paris, nous souhaitons sectoriser les annonces par arrondissement.

L’argument `place_ids` prendra donc successivement pour valeur les identifiants des arrondissements de Paris, séparés par une virgule (%2C dans l’URL) tels qu’indiqués dans le tableau ci-dessous. 

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


#### 1.1.3 - Pagination 

Les annonces sont affichées par pages de 12. Il faut donc parcourir toutes les pages de résultat afin de consulter l’ensemble des annonces (paramètre page dans l’URL). 
Le nombre de pages de résultat est différent pour chaque arrondissement : de zéro à plusieurs dizaines de pages. Il faudra imaginer un mécanisme s’adaptant au nombre de pages à parcourir. Il y a plusieurs manières de faire. 

### 1.2 Extraction des caractéristiques des annonces 

Pour chaque annonce, on est intéressé par les caractéristiques suivantes : 
- `listing_id` : identifiant de l’annonce pour MeilleursAgents 
- `place_id` : identifiant de l’arrondissement (celui passé en paramètre de la recherche)
- `price` : prix de mise en vente, en valeur entière d’euros 
- `area` : superficie du bien, en valeur entière de mètres carrés 
- `room_count` : nombre de pièces du bien, en valeur entière également ; 

L’extraction de ces caractéristiques doit être faite en Python, **avec les librairies et outils de votre choix**.
Exemples de librairies (à titre indicatif) : un parseur html comme le module lxml.html en Python, un langage de parcours de DOM : xpath, un langage de recherche de motifs : regexp (module re en Python). 

La superficie (area) et le nombre de pièces (room_count) ne sont pas des informations structurées. Elles doivent être extraites à partir du titre de chaque annonce : « 2 pièces de 46 m2 ». Attention aux appartements de 1 pièce qui sont notés « Studio ». 

### 1.3 - Structure les informations en base de données

L’information extraite du site web doit ensuite être stockée en base de données dans une ou plusieurs tables qui faudra définir au préalable. 
En plus de leurs caractéristiques, on veut aussi modéliser l’évolution des annonces dans le temps. Plus concrètement, on veut connaître : 

- la date de mise en ligne (ou au moins la date à laquelle on l’a vue pour la première fois),
- la date de retrait du site (ou au moins la dernière date à laquelle on l’a vue),
- l’historique complet des prix. 

Voici les informations requises pour se connecter au serveur de base de données : 

- type : Postgresql (module `psycopg2` en Python) 
- host : `localhost` 
- port: `5432` 
- user : `meilleursagents` 
- password : `pikachu42!@`
- database : `meilleursagents` 

## 2 - Restituer l’information 

La carte et l’histogramme présentés en introduction de ce document sont servis par une application web écrit en Python à l’aide du micro-framework Flask. 

L’application web est déjà fonctionnelle, il reste à l’alimenter en données correctes. 

### 2.1 - Cartographier les prix par arrondissement 

Au chargement de la page web, le code JavaScript en charge de la génération de la carte interroge l’application web afin d’obtenir la liste des entités géographiques à afficher. L’application web fournit en retour une structure de données au format GeoJSON contenant la liste des arrondissements à afficher, leur forme géométrique ainsi qu’un prix moyen, définit aléatoirement pour le moment. La couleur de la forme géométrique dépend du prix de l’arrondissement qu’elle représente, selon la même échelle de couleurs que celle actuellement utilisée pour la carte de Paris sur le site web de MeilleursAgents. 

Il ne reste donc plus qu’à calculer, pour chaque arrondissement, le prix moyen par mètre carré réel et à intégrer ce résultat dans la réponse de l’application web au code JavaScript en charge de la génération de la carte. 

### 2.2 - Afficher des statistiques par arrondissement 

Lorsque l’on clique sur un arrondissement, un histogramme apparaît. Cet histogramme représente la distribution du volume d’annonces par gamme de prix dans cet arrondissement. De la même manière que précédemment, le code JavaScript en charge de la génération de cet histogramme interroge l’application web avant chaque affichage, en passant le code de l’arrondissement en paramètre. L’application web fournit en retour une structure de données au format JSON contenant, entre autres, les valeurs de chacune des barres de l’histogramme. L’axe des ordonnées est alors mis à l’échelle automatiquement en fonction des valeurs fournies. 

Il ne reste donc plus qu’à calculer, pour l’arrondissement ciblé, la distribution des annonces par gammes de prix et à l’intégrer à la réponse de l’application web au code JavaScript en charge de la génération de l’histogramme. 

### 2.3 - Afficher le prix moyen de l’arrondissement (bonus) 

Entre la carte et l’histogramme, nous n’affichons nulle part le prix moyen de l’arrondissement de manière numérique. Que faut-il faire pour l’afficher sur la page web lorsqu’on clique sur un arrondissement de la carte ?
