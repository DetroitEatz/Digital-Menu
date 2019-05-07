Digital QSR Menus
=====

Installation
------------
1. From https://github.com/DetroitEatz/Digital-Menu, click the green _*Clone or Download*_ button. 
2. Click the _*Download zip*_ button.
3. Once the code has been downloaded, move it to a directory on your local system where you would like to keep it. A good choice might be your local user home directory. 
4. Unzip the downloaded file by double-clicking and waiting for the zip file to open.
5. There will now be a directory with the same name as the zip file, IE: likely named **Digital-Menu**.
6. Navigate into the **Digital-Menu** directory you just created. Double-click on the file named **install.command**.
7. In the terminal window that appears, type answers to the prompts. For example, you will be asked:

		a. To create an administrator user. One option would be to name this user "admin". 
		b. For an email address for your administrator user.
		c. For a password for your administrator user.
8. Upon successful installation, double-click the file named **run.command** to begin the application.
9. Navigate to `http://localhost:8000` in a browser to see the dashboard page. Navigate to `http://localhost:8000/admin` and sign in with the admin user you just created in order to begin the setup process. 



Basic Commands
--------------

Setting Up Your Users

* To create an **superuser account**, use this command:

    $ python manage.py createsuperuser
    
* To collect static files:

    $ python manage.py collectstatic
    
* To create database changes

    $ python manage.py migrate
    
* To start server

    $ python manage.py runserver
    
Admin capabilities
------------------

* Create Displays
* Create Menus
* Associate Menus to Displays

General Capabilities
--------------------
* Change the status of items on display. 



