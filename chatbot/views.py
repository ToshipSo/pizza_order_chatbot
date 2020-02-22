from django.http import JsonResponse
from rest_framework.views import APIView
from .chat_response import get_response
from .models import Response, Toppings, Order, Size
from django.db.models import Sum
import re
import random


# Create your views here.
class ChatAPI(APIView):

    def post(self, request):
        session = request.session
        context = int(session.get('context', 0))
        text = str(request.data['text'])
        context_change = True
        response = ''
        payload = ' '
        if context == Response.WELCOME:
            context = get_response(text)
            if context == Response.FALLBACK:
                response = select_random_response(Response.FALLBACK)
                context = Response.WELCOME
            context_change = False
        elif context == Response.TAKE_SIZE and re.findall(create_regex(Size, 'size'), text):
            request.session['size'] = re.findall(create_regex(Size, 'size'), text)[0]
            toppings = Toppings.objects.values_list('topping', flat=True)
            payload = 'We have '
            for topping in toppings:
                payload += str(topping) + ', '
            payload = payload[:-2] + '.'
        elif context == Response.TAKE_TOPPINGS and re.findall(create_regex(Toppings, 'topping'), text):
            request.session['toppings'] = re.findall(create_regex(Toppings, 'topping'), text)
            payload = '(Enter quantity in integer value.)'
        elif context == Response.TAKE_QUANTITY and re.findall('\d+', text):
            request.session['quantity'] = re.findall('\d+', text)[0]
        elif context == Response.TAKE_NAME:
            request.session['name'] = text
        elif context == Response.TAKE_ADDRESS:
            request.session['address'] = text
            price = Size.objects.filter(size=request.session['size']).first().price
            price += Toppings.objects.filter(topping__in=list(session['toppings'])).aggregate(Sum('price'))[
                'price__sum']
            price *= int(session['quantity'])
            response = "That will be: " + str(price) + "Rs. \n Shall I confirm it."
        elif context == Response.TAKE_CONFIRMATION:
            print(1)
            if re.findall('yes|yep|sure|great|yeah|ok|okay|cool', text.lower()):
                print(2)
                size = Size.objects.filter(size=session['size']).first()
                print(3)
                toppings = Toppings.objects.filter(topping__in=list(session['toppings']))
                print(3)
                order = Order(name=session['name'], address=session['address'], quantity=session['quantity'], size=size)
                print(4)
                order.save()
                print(5)
                order.toppings.add(*list(toppings))
                print(6)
                response = 'Thanks for ordering with us. Your Order No is: ' + str(order.order_id)
                print(7)
                context = Response.WELCOME
                print(8)
                context_change = False
            elif re.findall('no|nah|never', text.lower()):
                context = Response.TAKE_SIZE
                context_change = False
                response = "Okay, Let's rebuild your order again. Tell me the pizza size again."
                clear_session(request)
            else:
                response = select_random_response(Response.FALLBACK)
                context_change = False
        elif context == Response.GET_STATUS and re.findall('\d{2,7}', text):
            order_no = int(re.findall('\d{2,7}', text)[0])
            order = Order.objects.filter(order_id=order_no).first()
            if order:
                response = 'Your Order is ' + order.status
                context = Response.WELCOME
                context_change = False
            else:
                response = 'Please enter correct Order number.'
                context_change = False
        else:
            response = select_random_response(Response.FALLBACK)
            context_change = False

        if context_change:
            context += 1
        session['context'] = context

        if response == '':
            response = select_random_response(context) + payload

        return JsonResponse({
            'text': response
        })


class ClearSessionAPI(APIView):
    def get(self, request):
        clear_session(request)
        if request.session.get('context', 0): del request.session['context']
        return JsonResponse({
            'clear': 'OK'
        })


def clear_session(request):
    if request.session.get('size', 0): del request.session['size']
    if request.session.get('toppings', 0): del request.session['toppings']
    if request.session.get('quantity', 0): del request.session['quantity']
    if request.session.get('name', 0): del request.session['name']
    if request.session.get('address', 0): del request.session['address']


def select_random_response(context):
    response = Response.objects.filter(context=context).all()
    random_response = random.choices(response)[0]
    return random_response.response


def create_regex(model, field_name):
    values = model.objects.values_list(field_name, flat=True)
    regex = ''
    for value in values:
        regex += str(value) + '|'
    return regex[:-1]
