from django.test import TestCase
from restaurant.models import Menu

# TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=8, inventory=90)
        self.assertEqual(str(item), "IceCream : 8")