# Pizza order chatbot
A chat-bot to order pizza.

## Requirements
* Python 3.6+
* Django
* DjangoRestFramework
* SQLite3
* NLTK

## Easy Run
#### Windows
* Run `setup.bat` file to setup and run server
#### Linux
* Run `setup.sh` file to setup and run server

Run `python manage.py createsuperuser` to create Admin User

## Manual Setup
* Create python virtual environment if needed.
* Run `pip install -r requirement.txt` to download dependencies.
* Run `python manage.py migrate` to setup database.
* Run `python manage.py loaddata db.json` to populate database with basic responses and other data.
* Run `python manage.py createsuperuser` to create Admin User
* Run `python manage.py runserver` to run server.

## Usage
* Ask bot to take your order and start telling him the requirements
    * Eg: `I would like to order pizza.`
    
* Ask bot that you want to know your order status.
    * Eg: `Can I my pizza status?`
    
* Access admin page on `<hostname>/admin`
    * You can see orders and update order status from Admin Panel.
    * You can add more Chat-bot responses from Admin Panel.
    * You can add more pizza toppings and size from Admin Panel.

## Sample Workflow
* User: Hey
* Bot: Hi there, How may I help you?
* User: I would like to order pizza.
* Bot: Sure, What pizza size do you want?
* User: I prefer large pizza.
* Bot: Okay, Which toppings? We have paneer, olive, tomato.
* User: I like paneer and olives.
* Bot: Nice, How many pizza do you want?
* User: I want 2 pizza. (Provide quantity in integer)
* Bot: Great, Can you tell me your name?
* User: Sam (Provide Name only)
* Bot: Where do you want it to be delivered?
* User: 401, Shayam Nagar (Provide Address only)
* Bot: That will be: 800Rs. Shall I confirm it.
* User: Sure.
* Bot: Thanks for ordering with us. Your Order No is: 1380165
* User: What is my order status?
* Bot: Sure, What pizza size do you want?
* User: Here it is. 1380165
* Bot: Your Order is Placed.

## Train Model
* You can add more user speeches to `trainingSet.csv` file and run `create_classifier.py` to create classifier.
* Run `create_classifier.py` file separately when server is not running.
* `create_classifier.py` will create classifier and save it in `media` folder so it can be used by Django server.

## Application Architecture
Naive Bayes Classifier is used to predict user's text context.
Server predicts the context and based on that chooses a random response from database.
App uses REST API to communicate to server and uses session to remember context during multiple REST requests.
Regular expression is used to take order details.