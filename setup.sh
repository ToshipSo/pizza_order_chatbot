if [ -d "$venv"]
then
virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py loaddata db.json
fi
source venv/bin/activate
python3 manage.py runserver


