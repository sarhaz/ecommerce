from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    image = models.ImageField(upload_to='media/category')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id']),
        ]


class PriceType(models.TextChoices):
    DOLLAR = '$', '$'


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media/product")
    price = models.PositiveBigIntegerField(default=0)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    count = models.PositiveBigIntegerField(default=0)
    price_type = models.CharField(max_length=100, choices=PriceType.choices)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=20)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        indexes = [
        models.Index(fields=['id']),
        ]


class Logos(models.Model):
    image = models.ImageField(upload_to='media/logos')

    class Meta:
        ordering = ['id']
        indexes = [
        models.Index(fields=['id']),
        ]



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    shipping = models.DecimalField(max_digits=10, decimal_places=2, default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"name: {self.products.name}"

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id']),
        ]


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id']),
        ]


class Checkout(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id']),
        ]


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id']),
        ]
