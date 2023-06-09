from django.urls import path
from account import views

urlpatterns = [
    path("login/", views.login_user, name = "login"),
    path("signup/", views.register_user, name = "register"),
    path("logout/", views.logout_user, name = "logout")
]
