
from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.listTask,name="list_task"),
    path('update-task/<str:pk>/',views.updateTask,name="update"),
    path('delete-task/<str:pk>/',views.deleteTask,name="delete_task"),
    path('login/',views.sign_in,name="login"),
    path('logout/',views.sign_out,name="logout"),
    path('register/',views.sign_up,name="register"),
    path('account/',views.account,name="account"),
    path('deletetask/<int:pk>',views.deleteTask,name="confirm_delete"),
    # path('lock/',views.lock,name="lock"),
    # path('unlock/',views.unlock,name="lock"),
]
