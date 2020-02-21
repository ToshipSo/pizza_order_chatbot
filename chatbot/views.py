from django.http import JsonResponse
from rest_framework.views import APIView
from .chat_response import get_response


# Create your views here.
class ChatAPI(APIView):

    def get(self, request):
        print(get_response(request.query_params['text']))
        return JsonResponse({
            'context': get_response(request.query_params['text']),
            'text': 'Hey'
        })
