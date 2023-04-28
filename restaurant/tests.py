from django.test import TestCase
from .models import Booking, Menu
# Create your tests here.


class BookingTestCase(TestCase):
    def setUp(self):
        Booking.objects.create(first_name="Cris")
        Booking.objects.create(reservation_date="07/01/2023")
        Booking.objects.create(reservation_slot=4)

    def MenuTestCase(self):
        name = Menu.objects.get(name="lasagna")
        price = Menu.objects.get(price=5.99)
        menu_item_description = Menu.objects.get(description= "Italian Dish")

