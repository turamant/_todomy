from django.urls import path

from todos.views import DetailTodoView, ListTodoView

urlpatterns = [
    path('<int:pk>/',DetailTodoView.as_view(), name='detail'),
    path('',ListTodoView.as_view(), name='list_api'),
]