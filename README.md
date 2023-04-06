# H1 Initialisation du projet avec Django REST Framework et Vue.js 3
Ce projet utilise Django REST Framework pour l'API backend et Vue.js 3 pour le frontend. L'arborescence du projet est divisée en deux dossiers: "backend" pour l'API et "front" pour le frontend.

## H2 Installation des dépendances
### H3 Backend
Dans le dossier "backend", exécutez la commande suivante pour installer les dépendances Python:
`pip install -r requirements.txt`

### H3Frontend
Dans le dossier "front", exécutez la commande suivante pour installer les dépendances Node.js:
 `npm i` 
 
## H2 Configuration de l'API backend
Avant de lancer le serveur backend, vous devez configurer l'API. Copiez le fichier ".env.example" et renommez-le en ".env". Dans ce fichier, vous pouvez définir les variables d'environnement pour l'API, telles que la base de données, les clés d'API, etc.

## H2 Lancement de l'API backend
Dans le dossier "backend", exécutez la commande suivante pour lancer le serveur backend:
`python manage.py runserver`
Le serveur backend sera accessible à l'adresse suivante: http://localhost:8000/

## H2 Lancement du frontend
Dans le dossier "front", exécutez la commande suivante pour lancer le serveur frontend:

`npm run serve`
Le serveur frontend sera accessible à l'adresse suivante: http://localhost:8080/

Vous pouvez maintenant accéder à l'application en ouvrant votre navigateur et en naviguant vers http://localhost:8080/.
