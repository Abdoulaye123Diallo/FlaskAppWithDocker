from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Connexion à MySQL
db = mysql.connector.connect(
    host="mysql-db",   # Nom du service MySQL dans le réseau Docker
    #port=3308,
    user="root",
    password="admin",
    database="flask_db"  # Assurez-vous que la base existe
)

cursor = db.cursor()

# Créer la table étudiants si elle n'existe pas
cursor.execute("""
CREATE TABLE IF NOT EXISTS etudiants (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    age INT
)
""")
db.commit()

# Route pour ajouter un étudiant
@app.route('/add', methods=['POST'])
def add_etudiant():
    data = request.json
    id = data["ID"]
    nom = data['nom']
    age = data['age']
    
    query = "INSERT INTO etudiants (id, nom, age) VALUES (%s, %s, %s)"
    values = (id, nom, age)
    cursor.execute(query, values)
    db.commit()
    
    return jsonify({'message': 'Étudiant ajouté avec succès'}), 201

# Route pour récupérer les étudiants
@app.route('/etudiants', methods=['GET'])
def get_etudiants():
    cursor.execute("SELECT * FROM etudiants")
    rows = cursor.fetchall()
    
    result = []
    for row in rows:
        result.append({'ID': row[0], 'nom': row[1], 'age': row[2]})
    
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
