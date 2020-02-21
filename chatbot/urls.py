from django.urls import path
from django.views.generic import TemplateView
from chatbot import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html')),
    path('chat', views.ChatAPI.as_view())
]
