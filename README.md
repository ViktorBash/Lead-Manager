# Lead-Manager
This is a lead manager that allows you to track leads. It is built with React and Redux on the frontend, with Django Rest Framework on the backend.

## How To Run
* `npm i` - to install the nodejs dependencies.

* `pip install -r requirements.txt` it is recommended you also make your own virtual environment for the project.

* The project is configured for both PostgreSQL and SQLite.
    * For SQLite: uncomment the SQLite `DATABASES` code in `settings.py` and comment out the PostgreSQL `DATABASES` code.
    * For PostgreSQL: Connect to a PostgreSQL server and change `DATABASES` in `settings.py` if need be. Download PostgreSQL and pgAdmin to create a local PostgreSQL server.

* `python manage.py makemigrations` and `python manage.py migrate` to create the database.

* `npm run dev` or `npm run build`. Then in another terminal in the same directory run `python manage.py runserver`. Your server should now be on localhost:8000 or your IP address.
