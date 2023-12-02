from django.test import TestCase
from restaurant.models import Menu, Bookings, Cart, Orders
from django.contrib.auth.models import User
from datetime import date
from rest_framework.test import APITestCase
""" module to for test cases """


class MenuTest(TestCase):
    """ test Menu """
    def test_menuCreate(self):
        """ test create menu item """
        menu = Menu.objects.create(menuItem= 'choco', price=50)
        self.assertEqual(str(menu), 'choco: 50$')
    
class MenuTestApi(APITestCase):
    def test_routeMenu(self):
        """ test """
        data = {
            "id": 2,
            "menuItem": "cake",
            "description": "nice cake",
            "price": 50
        }
        self.client.post('/api/menu/', data=data)
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0], data)

class BookingTest(TestCase):
    """ test Booking """
    def test_bookingCreate(self):
        """ test create a booking """
        booking = Bookings.objects.create(name='James', slots=3, date=date(2023, 12, 5))
        self.assertEqual(str(booking), 'booking name: James')


class BookingTestApi(APITestCase):
    def test_routeBooking(self):
        """ test """
        data = {
            "id": 2,
	        "name": "Mai",
	        "slots": 3,
	        "date": "2023-12-05"
        }
        self.client.post('/api/bookings/', data=data)
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0], data)