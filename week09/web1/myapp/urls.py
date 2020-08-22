from django.urls import path
from . import views

urlpatterns = [
    path('wrong_password', views.wrong_password),
    path('logged_in', views.logged_in),
    path('', views.login2)
]
