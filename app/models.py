from django.contrib.auth.models import AbstractUser
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class User(AbstractUser):
    customer_types = (
        ("user", "user"),
        ("manager", "manager"),
    )
    role = models.CharField(max_length=120, choices=customer_types, default="user")


class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField()
    is_premium = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")


class ProductVideo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    video = models.FileField(upload_to="videos/", verbose_name="Video", null=True,)
