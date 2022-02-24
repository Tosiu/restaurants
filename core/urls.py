from django.urls import path
from core import views

urlpatterns = [
    path("", views.home, name="home"),
    path('login', views.login, name='login'),
    path('add_restaurant', views.add_restaurant, name='add_restaurant'),
    path('pick_restaurant', views.pick_restaurant, name='pick_restaurant'),
]

