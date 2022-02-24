from django.urls import path
from api import views

urlpatterns = [
    path("pick_restaurant", views.pick_restaurant, name="pick_restaurant"),
    path("add_restaurant", views.add_restaurant, name="add_restaurant"),
    path("auth", views.auth, name="auth"),
    path("sign_out", views.sign_out, name="sign_out"),
]

