Application is deployed on heroku's cloud services
https://edbrgapp.herokuapp.com/response

Steps for running the app:
    1. Unzip the file DjangoFormsBasics.zip as DjangoFormsBasics folder
       
    2. Folder structure
	DjangoFormsBasics
	- manage.py
	- DjangoFormsBasics
		- wsgi.py
	   	- __init__.py
	   	- settings.py
	   	- urls.py
	- responseapp
	   	-tests.py
	   	- __init__.py
	   	- apps.py
	   	- admin.py
	   	- templates
	   	- migrations
	   	- forms.py
	   	- urls.py
   		- est.py
   		- models.py
   		- views.py
	- runtime.txt
	- requirements.txt
	- db.sqlite3
	- Procfile
	- ReadMe
    3. Install python 3.6.x
    4. Install python libraries mentioned in requirements.txt
    5. Run “manage.py” as “python  manage.py migrate” to intialize changes made in the app
    6. To start the app server run “python  manage.py runserver”.
    7. Open the link “http://localhost:8000/response/” in browser to see the app in action.
