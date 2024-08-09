import secrets
from urllib import request
from django.conf import settings
from django.db import models
from django.forms import ValidationError
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from PIL import Image
import requests # type: ignore

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    image = models.ImageField(upload_to="menu-image/", default='../static/images/Eba.jpg')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    popular = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Recipes"
        ordering = ['-date_created', '-date_updated']
        
    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Menu, self).save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        
        if img.height >= 250 and img.width >= 250:
            output = (250,250)
            img.thumbnail(output)
            img.save(self.image.path)
            
    def get_absolute_url(self):
        return reverse("menu_details", kwargs={"pk": self.pk})
    
def check_pin_code(value):
    if not value.is_digit():
        raise ValidationError("Invalid pin code")
    else:
        pass

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pin_code = models.CharField(max_length=6)
    landmark = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username
    
    
    class Meta:
        ordering = ['-date_created', '-date_updated']
    
        
    
class Cart(models.Model):
    name = models.CharField(max_length=100, default="gold")
    checker = models.BooleanField(default=False, editable=False)
    is_paid = models.BooleanField(default=False)
    ref = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def get_cart_total(self):
        print(self.cartitem_set.all())
        cart_items = self.cartitem_set.all()
        price = []
        
        for cart_item in cart_items:
            price.append(cart_item.get_current_price())
        print(price)
        return sum(price)
        
    def save(self, *args, **kwargs):
        try:
            while not self.ref:
                ref = secrets.token_urlsafe(50)
                similiar_ref = Cart.objects.filter(ref=ref)
                
                if not similiar_ref:
                    self.ref = ref
            
            super().save(*args, **kwargs)
        except Exception as e:
            print(e)
    
    def verify_payment(self):
        base_url = 'https://api.paystack.co'
        path = f"/transaction/verify/{self.ref}"

        headers = {
            "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
            'Content-Type': 'application/json',
        }

        url = base_url + path
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            return response_data['status']
        response_data = response.json()
        return response_data['status']

    def __str__(self) -> str:
        return self.name
    
class CartItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def get_current_price(self):
        return self.quantity * self.menu.price
    
    def __str__(self) -> str:
        return self.menu.name
    
    class Meta:
        verbose_name = "Cart Item"
        ordering = ['-date_created', '-date_updated']