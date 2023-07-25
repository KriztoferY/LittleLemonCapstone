from django.test import TestCase

from restaurant.models import Menu


class MenuViewTest(TestCase):
    def setUp(self) -> None:
        item1 = Menu.objects.create(title="Ice cream", price=10, inventory=100)
        item2 = Menu.objects.create(title="Sandwich", price=5, inventory=10)
        item3 = Menu.objects.create(title="Chips", price=4, inventory=30)

    def test_getall(self):
        items = Menu.objects.all()
        self.assertEqual(len(items), 3)
