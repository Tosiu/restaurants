from django.contrib import messages
from django.core import serializers
from django.core.exceptions import ValidationError
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect
import json
from datetime import datetime, timedelta
from api.models import Restaurant, Visit


def pick_restaurant(request):
    if not request.user.is_authenticated:
        return redirect_to_login(request)
    else:
        if not Restaurant.objects.all():
            return HttpResponse('Apologizes, there are no restaurants in our database yet')
        start_of_week = datetime.now() - timedelta(days=datetime.now().weekday())
        this_week_visits = Visit.objects.filter(user__username=request.user, date__gte=start_of_week).values_list('restaurant', flat=True)
        possible_choices = Restaurant.objects.exclude(id__in=this_week_visits)
        if not possible_choices:
            possible_choices = Restaurant.objects.all()
        random_restaurant = possible_choices.order_by('?').first()
        new_visit = Visit(restaurant=random_restaurant, date=datetime.now(), user=request.user)
        new_visit.save()
        single_obj = model_to_dict(random_restaurant)
        return JsonResponse(single_obj)


@require_http_methods(["POST"])
def add_restaurant(request):
    if not request.user.is_authenticated:
        return redirect_to_login(request)
    else:
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            restaurant = Restaurant(
                name=body['name'],
                url=body['url'],
                phone=body['phone'],
                notes=body['notes']
            )
            try:
                restaurant.full_clean()
                restaurant.save()
                return HttpResponse('Restaurant saved', status=200)
            except ValidationError as e:
                return HttpResponse(e, status=400)
        except KeyError as e:
            return HttpResponse(f"Couldn't find {e} in form request", status=400)


@require_http_methods(["POST"])
def auth(request):
    try:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        username = body['username']
        password = body['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse(
                {
                    'bar': 'foo'
                }
            )
        else:
            return HttpResponse('Unauthorized', status=401)
    except KeyError as e:
        return HttpResponse(f"Couldn't find {e} in form request", status=400)


def sign_out(request):
    logout(request)
    return HttpResponse('User signed out')


def redirect_to_login(request):
    messages.error(request, 'Access denied')
    return redirect('/login')