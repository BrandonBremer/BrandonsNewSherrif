from django.test import TestCase
from shop.models import Post, Food
from django.contrib.auth.models import User
from shop.forms import *

#test
class testFood(TestCase):
    def testFood_Creation(self):
        f1 = Food.objects.create(item_name = "Food1", item_price = "9.99")
        f1.save()
        self.assertTrue(isinstance(f1, Food))
    def test_food_values(self):
        f1 = Food.objects.create(item_name = "Food1", item_price = "9.99")
        f2 = Food.objects.create(item_name = "Food1", item_price = "9.99")
        f1.save()
        f2.save()
        self.assertTrue(isinstance(f1, Food))
        self.assertTrue(isinstance(f2, Food))
        self.assertNotEqual(f1,f2)

    def test_edge_cases1(self):
        f1 = Food.objects.create(item_name="", item_price=0)
        f1.save()
        self.assertTrue(isinstance(f1, Food))

#test
class testViewallPosts(TestCase):
    def test_Location1(self):
        form = LocationForm()
        self.assertTrue(form.fields['location_choice'].label == None or form.fields['location_choice'].label == 'Filter by Location')

    def test_Location2(self):
        form = LocationForm()
        self.assertTrue(form.fields['sorter'].label == None or form.fields['sorter'].label == 'Show First:')
    def test_Location_valid(self):
        form = LocationForm(data={'location_choice': 'JPA', 'sorter':'bounty'})
        self.assertTrue(form.is_valid())


#test
class testPostForm(TestCase):
    def test_postForm(self):
        form = PostForm(data={'location_choice': 'JPA'})
        self.assertFalse(form.is_valid())

