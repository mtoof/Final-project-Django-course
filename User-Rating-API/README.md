### User Rating API

- In this little API, I used authentication and validation mechanisms inside Django REST Framework(DRF) to create a user rating API.
- The goal of this API is to recieve user review for menu items of a restaurant.
- Used the Djoser and authtoken packages for default routes and token authentication
- Used the Django admin panel for creating new users and tokens
- User can only rate a menu item once

Installation
------------

**Pipenv can be installed with Python 3.7 and above. For see the result of this little project you need python 3.9 **

For most users, I recommend installing Pipenv using `pip`:

    pip install --user pipenv

Install requirements:
    pipenv install

Go to the virtual environment:
    pipenv shell

You need to migrate

    python3 manage.py makemigrations
    python3 manage.py migrate

You need to create a super user to add menuitems and users

    python3 manage.py createsuperuser
    python3 manage.py runserver


Go to the URL: http://127.0.0.1:8000/admin and login with the super user username and password you created.
You need to add some menuitems and users in the admin panel, then add tokens for the users.


Create a POST request to the URL: http://127.0.0.1:8000/api/ratings
Now open the API request client, Insomnia and perform the following actions:

 - You need to add the token to the header of the request. Add Authorization as key and Token as value.
 - You can use a software like Postman or Insomnia to send the request.


Add menuitem_id as key and small integer as value, add rating as key and 0-5 as value
