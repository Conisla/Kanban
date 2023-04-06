# H1 Initialisation du projet avec Django REST Framework et Vue.js 3
Ce projet utilise Django REST Framework pour l'API backend et Vue.js 3 pour le frontend. L'arborescence du projet est divisée en deux dossiers: "backend" pour l'API et "front" pour le frontend.

Installation des dépendances
Backend
Dans le dossier "backend", exécutez la commande suivante pour installer les dépendances Python:

Copy code
pip install -r requirements.txt
Frontend
Dans le dossier "front", exécutez la commande suivante pour installer les dépendances Node.js:

css
Copy code
npm i
Configuration de l'API backend
Avant de lancer le serveur backend, vous devez configurer l'API. Copiez le fichier ".env.example" et renommez-le en ".env". Dans ce fichier, vous pouvez définir les variables d'environnement pour l'API, telles que la base de données, les clés d'API, etc.

Lancement de l'API backend
Dans le dossier "backend", exécutez la commande suivante pour lancer le serveur backend:

Copy code
python manage.py runserver
Le serveur backend sera accessible à l'adresse suivante: http://localhost:8000/

Lancement du frontend
Dans le dossier "front", exécutez la commande suivante pour lancer le serveur frontend:

arduino
Copy code
npm run serve
Le serveur frontend sera accessible à l'adresse suivante: http://localhost:8080/

Vous pouvez maintenant accéder à l'application en ouvrant votre navigateur et en naviguant vers http://localhost:8080/.
