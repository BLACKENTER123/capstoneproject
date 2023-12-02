from django.db import models
from django.contrib.auth.models import User

class Menu(models.Model):
    """ class for the Menu"""
    menuItem = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=500, null=False)
    price = models.IntegerField(null=False)

    def __str__(self):
        """ string representation item: 5$ """
        return self.menuItem + ': ' + str(self.price) + '$'

class Bookings(models.Model):
    """ class for bookings """
    name = models.CharField(max_length=200)
    slots = models.IntegerField(default=2)
    date = models.DateField(null=False)

    def __str__(self):
        """ string booking name: name """
        return 'booking name: '+ self.name

class Cart(models.Model):
    """ cart """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    totalprice = models.DecimalField(decimal_places=2, max_digits=65)

    def __str__(self):
        """ cart representation """
        return 'cart for: ' + str(self.user)

class Orders(models.Model):
    """ Order """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')
    crew_member = models.ForeignKey(User, on_delete=models.CASCADE, related_name='crew', default=2)
    status = models.BooleanField(default=False)
    totalPrice = models.DecimalField(decimal_places=2, max_digits=65)
    def __str__(self):
        """ string related user name """
        return 'order by: ' + str(self.user)

class OrderItem(models.Model):
    """ orderItem """
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='orderItem')
    item = models.ForeignKey(Menu, on_delete=models.CASCADE) 
    quentity = models.IntegerField()
    totalPrice= models.DecimalField(max_digits=65 ,decimal_places=2)

    def __str__(self):
        """ string order number: order """
        return str(self.order)