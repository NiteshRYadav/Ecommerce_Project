from django.contrib import admin
from .models import *

admin.site.register((
                    Wishlist,
                    Checkout,
                    Subscribe,
                    Contact))

@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name","basePrice","discount","finalPrice","color","size","description","stock","time","pic1","pic2","pic3","pic4")

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ("id", "name","username","email","phone","addressline1","addressline2","addressline3","pin","city","state","pic")

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ("id", "name","username","email","phone","addressline1","addressline2","addressline3","pin","city","state","pic")   