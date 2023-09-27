from django.urls import path
from .views import home, create_task, edit_todo, delete_todo

urlpatterns = [
    path("", home, name="home"),
    path("create/", create_task, name='create_task'),
    path("edit/<int:pk>/", edit_todo, name='editcha'),
    path("delete/<int:pk>/" , delete_todo, name='deletcha')
]
