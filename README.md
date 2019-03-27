# Picture Site Using Django, mySQL and XAMPP

Built on Linux
--
https://www.apachefriends.org/download.html

sudo ./opt/lampp/manager-linux-x64.run
start mySQL Database and Apache Web Server
On browser go to  localhost/phpmyadmin
create a database with name Djangopictures
the database with the above name has been set to be used in DjangoPictureSite/picturesite/settings.py

sudo apt install python3-venv -y
git clone git://github.com/django/django ~/django-dev

Choose project folder.
 
    python3 -m venv my_env
    source my_env/bin/activate

    pip3 install --upgrade pip

    pip3 install -e ~/django-dev

    pip3 install mysqlclient pylint-django Pillow

    pylint --load-plugins pylint_django .

-- not needed if you clone the repo --
    django-admin startproject DjangoPictureSite 
    python3 manage.py migrate
    python3 manage.py createsuperuser --username=abc --email=email@email.em
    python3 manage.py startapp pictures
    python3 manage.py runserver


