# Requirements
* Python 3
* Django

# Easy Run
#### Windows
* Run `setup.bat` file to run server
#### Linux
* Run `setup.sh` file to run server

Run `python manage.py createsuperuser` to create Admin User


# Usage
* Ask bot to take your order and start telling him the requirements
* Eg: `I would like to order pizza.`
***
* Ask bot that you want to know your order status.
* Eg: `Can I my pizza status?`
***
* Access admin page on `<hostname>/admin`
* You can add more robot responses from admin UI.
* You can add more pizza toppings and size from admin UI.
* You can see orders and update order status from admin UI.

# Train Model
* You can add more user speeches to `trainingSet.csv` file and run `create_classifier.py` to create classifier.
* Run `create_classifier.py` file separately when server is not running.
* `create_classifier.py` will create classifier and save it in `media` folder so it can be used by Django server.

# Manual Setup
* Create python virtual environment if needed.
* Run `pip install -r requirement.txt` to download dependencies.
* Run `python manage.py migrate` to setup database.
* Run `python manage.py loaddata db.json` to populate database with basic responses and other data.
* Run `python manage.py runserver` to run server.