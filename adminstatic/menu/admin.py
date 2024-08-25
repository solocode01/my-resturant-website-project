from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group

admin.site.unregister(Group)

# Register your models here.
class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1


@admin.register(Menu)
class Menuadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'popular', 'price', 'date_created', 'date_updated']
    list_display_links = ['slug']
    list_editable = ['name', 'price', 'popular']
    list_filter = ['price', 'slug', 'date_created', 'date_updated']
    list_per_page = 10
    inlines = [CartItemInline]
    search_fields = ['name', 'price', 'slug']
    fieldsets = (
        ("Recipe", {
            "fields": (
                'name', 'popular',
            ),
        }),
        
        ("Menu Details", {
            "fields": (
                "price", "description", 'image'
            ),
        }),
    )
    
    
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_paid', 'date_created', 'date_updated']
    inlines = [CartItemInline]
    
    
@admin.register(Customer)
class Customer(admin.ModelAdmin):
    list_display = ['user', 'address', 'street', 'city', 'date_created', 'date_updated']
    
    
admin.site.register(CartItem)