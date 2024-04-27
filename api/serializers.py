from rest_framework import serializers #jan 9
from django.contrib.auth.models import User
from api.models import Product,BasketItem,Basket

class UserSerializer(serializers.ModelSerializer):# jan9
    class Meta:
        model=User
        fields=['id','username','email','password']
        read_only_fields=['id']

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
    
class ProductSerializer(serializers.ModelSerializer):# jan9
    class Meta:
        model=Product
        fields="__all__"
        read_only_fields=['id','category']

    category=serializers.StringRelatedField()


# jan10
class BasketItemSerializer(serializers.ModelSerializer):
    product=ProductSerializer(read_only=True)
    class Meta:
        model=BasketItem
        fields="__all__"
        read_only_fields=[
            "id",
            "product",
            "is_active",
            "created_at",
            "updated_at",
            "total",
            "basket"
        ]
    total=serializers.IntegerField(read_only=True)#jan 11


#jan 11
class BasketSerializer(serializers.ModelSerializer):
    cart_items=BasketItemSerializer(read_only=True,many=True)
    owner=serializers.StringRelatedField()
    Basket_item_total=serializers.IntegerField(read_only=True)
    class Meta:
        model=Basket
        fields="__all__"
        read_only_fields=["id","owner","is_active","created_at","updated_at","cart_items"]

    