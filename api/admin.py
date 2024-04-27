from django.contrib import admin
from api.models import Category,Product,BasketItem,Basket
# register your models here
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(BasketItem)
admin.site.register(Basket)
