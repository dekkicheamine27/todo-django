from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add_todo', views.add, name="add_todo" ),
    path('remove/<int:todo_id>', views.remove, name="remove_todo"),
    
]
