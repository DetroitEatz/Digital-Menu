cd "`dirname "$0"`"
echo 'Installing virtualenv'
pip install virtualenv
echo 'Setup virtualenv'
virtualenv venv
echo 'Source venv'
source venv/bin/activate
pip install -r requirements/local.txt
echo 'Installation Completed'
#python manage.py migrate
#python manage.py collectstatic
#python manage.py createsuperuser
