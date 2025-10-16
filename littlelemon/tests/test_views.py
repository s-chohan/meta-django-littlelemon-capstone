from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer

# TestCase class
class MenuViewTest(TestCase):
    def setUp(self):
        # item1= Menu.objects.create(title="IceCream", price=8, inventory=90)
        item2 = Menu.objects.create(title="Pizza", price=9, inventory=20)
        item3 = Menu.objects.create(title="Burger", price=8, inventory=100)
    
    def test_getall(self):
        items = Menu.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        serialized_data = serializer.data # return seralized data in JSON
        expected_output = [{'id': 2, 'title': 'Pizza', 'price': '9.00', 'inventory': 20, 'menu_item_description': ''}, {'id': 3, 'title': 'Burger', 'price': '8.00', 'inventory': 100, 'menu_item_description': ''}]
        self.assertEqual(serialized_data, expected_output)
