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
7. After installation has completed, you can close the install window.
8. Double-click on the file named **run.command** to start the application. 
9. Navigate to `http://localhost:8000/admin` and sign in with the using the default username (`admin`) and password (`admin123`)
10. After setting up Screens, Menus, Slots, and Templates in the admin area, navigate to `http://localhost:8000/` to see the dashboard used to change menu status.

Running
-------
In the event the application dies (power outage, etc), simply start the application again by double-clicking the **run.command** file. 

From each physical display you'll need to connect to this application via a browser. If you have created a menu named "Menu1" that is meant to display on a particular display, you'll navigate to `http://<hostname>:8000/menu1` where <hostname> is the name of the hosting Mac Mini. 

Within the store, there will need to be a display connected to `http://localhost:8000/` where the status of menus can be seen and changed as needed. 
  
  
Admin capabilities
------------------

* Create Screens
* Create Menus
* Associate Menus to Screens
* Upload new Templates
* Associate Templates to Menus
* Set up Slots for a Menu


General Capabilities
--------------------
* Change the status of items on display. 


Technical Information
=====================

This is a standard Django / Python application that uses SqlLite as an embedded database. It ships with an existing database and page templates. 

Command Line Basics
-----------------------

Setting Up Your Users

* To create an **superuser account**, use this command:

    $ python manage.py createsuperuser
    
* To collect static files:

    $ python manage.py collectstatic
    
* To gather database changes

    $ python manage.py makemigrations
    
* To apply database changes

    $ python manage.py migrate
    
* To start server

    $ python manage.py runserver
    
Understanding the Data Models
-----------------------------

**Screen**
 A Screen represents a physical display. For future reference, we've included boolean fields for whether a display is inside or outside the building and whether it is orientated vertically.
 
**Menu**
 A menu represents the content to be displayed on a physical Screen. It has a template and may have a background image.
 
**Slot**
 A Slot represents a part of a Menu in which we want to have a visible status indicator. It can also have an image.
 
**Template**
A Template represents the visual layout that will be used by a Menu. It is the link to an actual html page. This is not to be confused with Django's built-in templates.  
  
  
Support
-------

support@mercenarytech.com
  