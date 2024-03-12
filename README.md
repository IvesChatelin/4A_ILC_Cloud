# Stack tech projet

- **Frontend** : Angular
- **Backend** : Flask
- **Database** : redis

# Docker
Le fichier docker-compose.yml contient le manifeste de tous les conteneur à construire. A la racine du dossier cloner, saisi la commande :
```
docker compose up
```
ou

```
docker-compose up
```

# Kubernetes
Le dossier Kubernetes contient les manifeste des objects `deployment` et `service NodePort`. les pods sont crées à partir des images crées localement avec le docker compose. 

La commande `kubectl apply -f deployment.yml` permet de créer l'objet `deployment` de l'application. 
la commande `kubectl apply -f service.yml` permet de créer un service `NodePort`.

l'application est accessible depuis le NodePort 30001
> localhost:30001

# Redis
Structure de la base de données :

- Une base de données pour stocker les tweets : `key=timestamp, value={“author”: "username", “tweet”: ”message”, "subject": "subject"}`
- Une base de données pour stocker la liste de clé des tweets :  `key=timestamps, values=[timestamp_1, timestamp_2, timestamp_3]`
- Une base de données pour stocker les utiliateurs par email : `key=email, value={"username":"username", "password":"pwd" }`
- Une base de données pour stocker les utiliateurs par username : `key=username, value={"email":"email", "password":"pwd" }`
- Une base de données pour stocker les clés des tweets liés à un sujet : `key=tweets:subject, value=[timestamp_1, timestamp_2, timestamp_3]`
- Une base de données pour stocker les clés des tweets liés à un utilisateur : `key=tweets:author, value=[timestamp_1, timestamp_2, timestamp_3]`
- Une base de données pour stocker le nom d'utilisateur et la clé du tweet liké : `key=liked_username:timestamp, value=[{"author": username, "timestamp": timestamp}]`
- Une base de données pour stocker le nom d'utilisateur et la clé du tweet retweeté : `key=retweeted_username:timestamp, value=[{"author": username, "timestamp": timestamp}]`