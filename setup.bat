IF NOT EXIST venv (
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata db.json
)
.\venv\Scripts\activate && python manage.py runserver