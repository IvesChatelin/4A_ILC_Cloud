## Stack tech projet

- **Frontend** : Angular
- **Backend** : Flask

# Docker
le fichier docker-compose.yml contient le manifeste de tous les conteneur à construire. A la racine du dossier cloner, saisi les etapes suivantes :
- **docker compose build** pour construire les images du backend et frontend
- **docker compose up** pour créer les conteneur
la commande **docker compose up** seul eput faire le build et lancer les comteneurs.

Attention!! si la commande docker compose je marche pas, utilisez la commande **docker-compose**. il est aussi préferable d'être dans un terminal linux (git bash, wsl, ...).

# Kubernetes
Le dossier Kubernetes contient les manifeste des objects **deployment** et **service NodePort**. les pods sont crées à partir des images crées dans le docker compose. 

la commande **kubectl apply -f manifeste** permet de créer les objets dans le cluster. 