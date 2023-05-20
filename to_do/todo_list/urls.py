from django.urls import path
from todo_list import views

urlpatterns = [
    path('create/', views.create, name = "create")
]