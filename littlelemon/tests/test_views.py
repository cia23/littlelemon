from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances of the Menu model
        self.item1 = Menu.objects.create(title="Ice Cream", price=3.00, inventory=100)
        self.item2 = Menu.objects.create(title="Pizza", price=12.00, inventory=50)
        self.item3 = Menu.objects.create(title="Burger", price=10.00, inventory=80)

    def test_getall(self):
        menus = Menu.objects.all()
        serialized_data = MenuSerializer(menus, many=True).data

        expected_data = [
            {"title": "Ice Cream", "price": "3.00", "inventory": 100},
            {"title": "Pizza", "price": "12.00", "inventory": 50},
            {"title": "Burger", "price": "10.00", "inventory": 80}
        ]

        # Sort both lists before comparison
        serialized_data.sort(key=lambda x: x['title'])
        expected_data.sort(key=lambda x: x['title'])
        
        self.assertEqual(serialized_data, expected_data)