from django.test import TestCase

from restaurant.models import Menu


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Ice cream", price=10, inventory=100)
        self.assertEqual(f'{item}', "Ice cream - $10")
