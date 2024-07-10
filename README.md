Créer et entrer dans le répertoire du projet.
Créer un environnement virtuel
python -m venv env
source env/scripts/activate

installer Django:
pip install django
Puis, créeons un fichier requirements.txt pour stocker les packages nécessaires.

Le projet est démarré avec la commande:
django-admin startproject portfolio .  (Le point pour la création dans le même rep.)
Cette commande crée un rep portfolio ainsi que l'executable manage.py

Django installe deux applications dans deux dossiers séparés:
	python manage.py startapp authentication
	python manage.py startapp blogapi
	

python manage.py runserver (pour démarrer le programme)
Accès page administrateur: http://127.0.0.1:8000/admin/	id: lou pass: edwood

Accès page web: http://127.0.0.1:8000/	id: lou pass: edwood


	


