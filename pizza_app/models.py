from django.db import models


# Create your models here.
class Pizza_Model(models.Model):
    name = models.CharField(max_length=10)
    price = models.CharField(max_length=10)


class User_Model(models.Model):
    user_id = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=10)


class Order_Model(models.Model):
    user_name = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=10)
    user_address = models.CharField(max_length=100)
    ordered_items = models.CharField(max_length=20)
    order_status = models.CharField(max_length=10)
