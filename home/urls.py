from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.listTask,name="list_task"),
    path('update-task/<str:pk>/',views.updateTask,name="update"),
    path('delete-task/<str:pk>/',views.deleteTask,name="delete_task"),
]
