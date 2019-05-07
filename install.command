cd "`dirname "$0"`"
echo  -e "\033[1mInstalling virtualenv\033[0m"
pip install virtualenv
echo -e "\033[1mSetup virtualenv\033[0m"
virtualenv venv
echo -e "\033[1mSource venv\033[0m"
source venv/bin/activate
pip install -r requirements/local.txt
python manage.py migrate
python manage.py collectstatic
#python manage.py createsuperuser

echo -e "\033[1mInstallation Completed\033[0m"
