### 1. Cloner le repository localement via cette commande :
git clone https://github.com/Abdoulaye123Diallo/FlaskAppWithDocker.git

Ensuite, se déplacer vers le repertoire ou se trouve le fichier docker-compose.yml via cette commande :
cd FlaskAppWithDocker

Exécuter cette commande pour lancer les applications :
docker-compose -f docker-compose.yml up

Une fois tout cela fait, ouvrir postamn pour faire les tests:
D'abourd exécuter cette curl pour ajouter un étudiant dans la base de données Mysql :

curl --location 'http://localhost:5000/add' \
--header 'Content-Type: application/json' \
--data '{
    "ID":1,
    "nom":"Abdoulaye Diallo",
    "age":23
}'
Si tout marche on devra voir le message : Etudiant ajouté avec succès

Pour tester la récupération des étudiants de la base, exécuter cette curl :
curl --location 'http://localhost:5000/etudiants'

