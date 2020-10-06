# Fonctionnement du projet

## Démarrer le projet
Lance les applications et la base de données.

```sh
make run
```

`ctrl + C` pour les stopper

## Reconstruire le projet
Normalement cette étape n'est pas nécessaire car effectuée automatiquement au démarrage des applications mais permet de forcer la reconstruction des applications.

```sh
make build
```

## Entrer dans le conteneur
Pour entrer dans le shell de l'application et taper des commandes manuelles

```sh
docker-compose run pricemap bash
```

Vous pouvez également le faire sur `listingapi` et `db` mais cela ne devrait pas être utile.

## Nettoyage
Détruit les conteneurs des applications. Utile car par défaut, `docker-compose` réutilise des conteneurs déjà lancés

```sh
make clean
```

Pour supprimer également les volumes de données des applications (pour être certain que votre base de données soit réinitialisée par exemple)
```sh
make clean-all
```
