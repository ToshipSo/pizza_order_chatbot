from django.http import JsonResponse
from rest_framework.views import APIView
from .chat_response import get_response
from .models import Response, Toppings, Order, Size
from django.db.models import Sum
import re


# Create your views here.
class ChatAPI(APIView):

    def create_regex(self, model, field_name):
        values = model.objects.values_list(field_name, flat=True)
        regex = ''
        for value in values:
            regex += str(value) + '|'
        return regex[:-1]

    def post(self, request):
        session = request.session
        context = int(session.get('context', 0))
        text = str(request.data['text'])
        response = ''
        if context == 0:
            context = get_response(text)
            if context == 10:
                response = Response.objects.filter(context=context).first().response
                context = 0
            # else:
            #     response = Response.objects.filter(context=context).first().response
        elif context == 1 and re.findall('(small|regular|medium|large)', text):
            request.session['size'] = re.findall('(small|regular|medium|large)', text)[0]
            context += 1
            # response = Response.objects.filter(context=context).first().response
        elif context == 2 and re.findall(self.create_regex(Toppings, 'topping'), text):
            request.session['toppings'] = re.findall(self.create_regex(Toppings, 'topping'), text)
            context += 1
            # response = Response.objects.filter(context=context).first().response
        elif context == 3 and re.findall('\d+', text):
            request.session['quantity'] = re.findall('\d+', text)[0]
            context += 1
            # response = Response.objects.filter(context=context).first().response
        elif context == 4:
            request.session['name'] = text
            context = context + 1
            # response = Response.objects.filter(context=context).first().response
        elif context == 5:
            request.session['address'] = text
            context += 1
            price = Size.objects.filter(size=request.session['size']).first().price
            price += Toppings.objects.filter(topping__in=list(session['toppings'])).aggregate(Sum('price'))[
                'price__sum']
            price *= int(session['quantity'])
            response = "That will be: " + str(price) + "Rs. \n Shall I confirm it."
        elif context == 6:
            if re.findall('yes|yep|sure|great|yeah|ok|okay|cool', text.lower()):
                size = Size.objects.filter(size=session['size']).first()
                toppings = Toppings.objects.filter(topping__in=list(session['toppings']))
                order = Order(name=session['name'], address=session['address'], quantity=session['quantity'], size=size)
                order.save()
                order.toppings.add(*list(toppings))
                context = 0
                response = 'Thanks for ordering with us. Your Order No is: ' + str(order.order_id)
            elif re.findall('no|nah|never', text.lower()):
                context = 1
                response = "Okay, Let's rebuild your order again. Tell me the pizza size again."
                clear_session(request)
            else:
                response = Response.objects.filter(context=10).first().response
        elif context == 7 and re.findall('\d{2,7}', text):
            order_no = int(re.findall('\d{2,7}', text)[0])
            order = Order.objects.filter(order_id=order_no).first()
            if order:
                response = 'Your Order is ' + order.status
                context = 0
            else:
                response = 'Please enter correct Order number.'
        else:
            response = Response.objects.filter(context=10).first().response

        if response == '':
            response = Response.objects.filter(context=context).first().response

        session['context'] = context
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
