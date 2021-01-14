from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
    item_name = models.CharField(max_length=200)
    item_price = models.FloatField(default=0.0)
    def __str__(self):
        return self.item_name

class Post(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    status = models.CharField(max_length=20)
    items = models.ManyToManyField(Food, through='Quantity')
    bounty = models.FloatField()
    location = models.CharField(max_length=50)
    dateposted = models.DateField(auto_now_add=True)
    daterequested = models.DateField()
    cost = models.FloatField()
    numitems = models.IntegerField()
    shopper = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shopper', null=True, blank=True)
    Location_Choices = (('BICE', 'Bice House'),('BOND', 'Bond House'),('BROWN', 'Brown College'),('COPELEY', 'Copeley Apartments'),('SHEA', 'French House/Spanish House/Shea House'),
                        ('GOOCH','Gooch Dillard/ Hereford'),('GRANDMARC', 'GrandMarc At the Corner'),('HEREFORD', 'Hereford College'),('IRC', 'International Residential College'),
                        ('JPA', 'JPA'),('LAMBETH', 'Lambeth Field Apartments'),('LARK', 'Lark on Main'),('NEW_DORMS', 'New Dorms'), ('OLD_DORMS', 'Old Dorms'),
                        ('PRESTON', 'Preston Avenue Area'),('FLATS', 'The Flats at West Village'),('LAWN', 'The Lawn'), ('STANDARD', 'The Standard'),)
    general_location = models.CharField(max_length = 100, choices = Location_Choices, default="JPA")

class Quantity(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity_food = models.IntegerField(default=0)
