from django.test import Client
from django.test import TestCase
from api.models import User
from payload import *
import copy


class ApiTestCase(TestCase):
    def setUp(self):
        self.c = Client()
        user = User.objects.create_user('test', password='password321')
        user.save()

    def test_bad_data_login(self):
        """ Test case that checks if we get 401 when user post bad login data"""
        response = self.c.post("/api/auth", incorrect_login_data, content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_bad_request_login(self):
        """ Test case that checks if we get Bad Request error when posting invalid form"""
        response = self.c.post("/api/auth", bad_form_data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b"Couldn't find 'username' in form request")

    def test_correct_login(self):
        """ Test case that checks if we login with good data"""
        response = self.c.post("/api/auth", proper_login_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_redirect_when_not_authenticated(self):
        """ Test case that checks if we get redirected, when we want to access api without being logged"""
        response = self.c.get("/api/pick_restaurant")
        self.assertEqual(response.url, "/login")

    def test_redirect_when_trying_to_add_new_restaurant(self):
        """ Test case to catch all errors that can occure when adding new restaurant"""
        response = self.c.post("/api/add_restaurant", {}, content_type='application/json')
        self.assertEqual(response.status_code, 302)


class AddingRestaurantTestCase(TestCase):

    def setUp(self):
        self.c = Client()
        user = User.objects.create_user('test', password='password321')
        user.save()
        self.c.post("/api/auth", proper_login_data, content_type='application/json')

    def test_bad_form_data(self):
        self.c.post("/api/auth", proper_login_data, content_type='application/json')
        response = self.c.post("/api/add_restaurant", {}, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b"Couldn't find 'name' in form request")

    def test_phone_number_too_big(self):
        case_specific_form = copy.deepcopy(restaurant1)
        case_specific_form['phone'] = '12345123451'
        response = self.c.post("/api/add_restaurant", case_specific_form, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_phone_number_include_letters(self):
        case_specific_form = copy.deepcopy(restaurant1)
        case_specific_form['phone'] = '12d123451'
        response = self.c.post("/api/add_restaurant", case_specific_form, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_adding_new_restaurant(self):
        response = self.c.post("/api/add_restaurant", restaurant1, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Restaurant saved")


class PickingRestaurantTestCase(TestCase):

    def setUp(self):
        self.c = Client()
        user = User.objects.create_user('test', password='password321')
        user.save()
        self.c.post("/api/auth", proper_login_data, content_type='application/json')

    def test_pick_when_0_restaurants_are_in_db(self):
        response = self.c.get("/api/pick_restaurant")
        self.assertEqual(response.content, b"Apologizes, there are no restaurants in our database yet")

    def test_pick_when_only_1_restaurant_is_in_db(self):
        self.c.post("/api/add_restaurant", restaurant1, content_type='application/json')
        response = self.c.get("/api/pick_restaurant")
        case_specific_form = copy.deepcopy(restaurant1)
        case_specific_form['id'] = 1
        self.assertEqual(response.json(), case_specific_form)
        response = self.c.get("/api/pick_restaurant")
        self.assertEqual(response.json(), case_specific_form)

    def test_pick_when_more_than_1_restaurant_are_in_db(self):
        self.c.post("/api/add_restaurant", restaurant1, content_type='application/json')
        self.c.post("/api/add_restaurant", restaurant2, content_type='application/json')
        self.c.post("/api/add_restaurant", restaurant3, content_type='application/json')
        list_of_ids = []
        response = self.c.get("/api/pick_restaurant")
        list_of_ids.append(response.json()['id'])
        response = self.c.get("/api/pick_restaurant")
        list_of_ids.append(response.json()['id'])
        response = self.c.get("/api/pick_restaurant")
        list_of_ids.append(response.json()['id'])
        self.assertEqual(sorted(list_of_ids), [1, 2, 3])
        response = self.c.get("/api/pick_restaurant")
        self.assertEqual(response.json()['id'] in [1, 2, 3], True)
