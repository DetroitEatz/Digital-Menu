echo -e "\033[1mDigital QSR Menus\033[0m"
echo -e "\033[1m Contact support@mercenarytech.com for support. \033[0m"

cd "`dirname "$0"`"
source venv/bin/activate
python manage.py runserver