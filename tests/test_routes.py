from django.test import TestCase
from shop.models import Food
# Create your tests here.

class RouteTests(TestCase):


    # This test ensures that the home route is properly connected to the home template.
    def test_home_route(self):
        response = self.client.get('')
        self.assertContains(response, "Login with Google")

    def test_shop_route(self):
        response = self.client.get('/shop/checkout')
        self.assertEqual(response.status_code, 301)

    #Check that the database exists
    def test_database(self):
        amount = Food.objects.all()
        Food.objects.create(item_name = "Pizza", item_price = 12.00)
        a = len(amount)
        self.assertTrue(a >= 0)


    def test_database_Pizza(self):
        amount = Food.objects.all()
        Food.objects.create(item_name = "Pizza", item_price = 12.00)
        c = Food.objects.get(item_name = "Pizza")
        self.assertNotEqual(c, None)

    def test_database_Pizza2(self):
        amount = Food.objects.all()
        Food.objects.create(item_name = "Pizza", item_price = 12.00)
        c = Food.objects.get(item_price = 12.00)
        self.assertEqual(c.item_price, 12.00)

    def test_filter(self):
        name = "Bread"
        Food.objects.create(item_name = name, item_price = 3.00)
        foods = Food.objects.filter(item_name__icontains=name)
        self.assertTrue(len(foods) == 1)

    def test_filter2(self):
        query = "Bread"
        Food.objects.create(item_name = "Bread", item_price = 3.00)
        Food.objects.create(item_name = "Special Bread", item_price = 6.00)
        Food.objects.create(item_name = "Moldy Bread", item_price = 1.00)
        Food.objects.create(item_name = "Pizza", item_price = 2.00)
        foods = Food.objects.filter(item_name__icontains=query)
        self.assertTrue(len(foods) == 3)

    def test_filter3(self):
        Food.objects.create(item_name = "Bread", item_price = 3.00)
        Food.objects.create(item_name = "Special Bread", item_price = 6.00)
        Food.objects.create(item_name = "Moldy Bread", item_price = 1.00)
        Food.objects.create(item_name = "Pizza", item_price = 2.00)
        foods = Food.objects.filter(item_name__icontains="")
        self.assertTrue(len(foods) == 4)
