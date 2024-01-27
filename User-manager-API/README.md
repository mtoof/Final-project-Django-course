### About this API
This API is a simple REST API that allows either a superuser or a user from `Manager` group to add or delete users from `Manager` or `Delivery crew` groups. A manager user can not delete his own account. A `Delivery crew` user can not delete his own account or any other user's account.

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

You need to create a super user and create some users

    python3 manage.py createsuperuser (It will ask you to enter a username, email and password)

    python3 manage.py runserver


Go to the URL: http://127.0.0.1:8000/admin and login with the super user username and password you created.
You need to add two groups `Manager` and `Delivery crew`, add some users using the admin panel, add one of them to the `Manager` group and don't assign the rest users to any groups, then add tokens for the users.

Now open the API request client app like Insomnia and perform the following actions:
Create a POST request to the URL: http://127.0.0.1:8000/api/token/user/ and add the following data to the body of the request:

	{
		"username": "username",
		"password": "password"
	}

This will return a token for the user. Copy the token.
Now open the API request client app like Insomnia and perform the following actions:
Create a POST request to the URL: http://127.0.0.1:8000/groups/manager/users/ or  http://127.0.0.1:8000/groups/delivery-crew/users/ and add the following data to the body of the request, You should be a superuser or a user from `Manager` group to perform this action, Add the token as key and `Token` as value. to the header of the request as well:

	{
		"username": "username",
	}

If it wass successful, you will get a response like this:

	{
		"message": "User added to the Manager group"
	}

You can also delete a user from the `Manager` or `Delivery crew` group by sending a DELETE request to the URL: http://127.0.0.1:8000/api/groups/manager/users/<id> or http://127.0.0.1:8000/groups/delivery-crew/users/<id>  There is not need to angle brackets, just add the id of the user you want to delete.
If it was successful, you will get a response like this:
	
	{
		"message": "User deleted from the Manager group"
	}

Again You should be a superuser or a user from `Manager` group to perform this action, Add the token as key and `Token` as value. to the header of the request as well.


Enjoy it!