from django.views.generic import TemplateView
from rest_framework import generics

from todos.models import Todo
from todos.serializers import TodoSerializer


class HomeView(TemplateView):
    template_name = 'home.html'

class ListTodoView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodoView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
