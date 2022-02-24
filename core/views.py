from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.http import JsonResponse
from django.views import generic
from django.contrib.auth.decorators import login_required


def home(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        return render(request, 'core/index.html')


def add_restaurant(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        return render(request, 'core/add_restaurant.html')


def pick_restaurant(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        return render(request, 'core/pick_restaurant.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'core/login.html')


def my_custom_page_not_found_view(request, exception):
    return render(request, 'core/404.html')

