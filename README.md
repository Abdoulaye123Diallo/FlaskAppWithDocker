# Flask App with Docker 🚀

Ce projet déploie une application Flask avec une base de données MySQL en utilisant Docker.

## Pré-requis 🛠️
Assurez-vous d'avoir les outils suivants installés sur votre machine :
- [Docker](https://docs.docker.com/get-docker/)
- [Git](https://git-scm.com/)

## Installation 🔧

1. **Clonez le repository localement :**

    ```bash
    git clone https://github.com/Abdoulaye123Diallo/FlaskAppWithDocker.git
    ```

2. **Accédez au répertoire du projet :**

    ```bash
    cd FlaskAppWithDocker
    ```

3. **Lancez les applications avec Docker Compose :**

    ```bash
    docker-compose -f docker-compose.yml up
    ```

## Tests via Postman 🔍

### Ajouter un étudiant 🧑‍🎓
Utilisez la commande `curl` ci-dessous pour ajouter un étudiant à la base de données MySQL :

```bash
curl --location 'http://localhost:5000/add' \
--header 'Content-Type: application/json' \
--data '{
    "ID": 1,
    "nom": "Abdoulaye Diallo",
    "age": 23
}'
```


### Récupérer les étudiants 👥
Exécutez cette commande pour obtenir la liste des étudiants dans la base de données :

```bash
    curl --location 'http://localhost:5000/etudiants'
```
