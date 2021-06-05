from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(User):
    mobile_no = models.IntegerField()
    age = models.IntegerField()


class Category(models.Model):
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="user_profile_category"
    )
    name = models.CharField(max_length=50)


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category_products"
    )
    name = models.CharField(max_length=50)
