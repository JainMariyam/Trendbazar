from django.shortcuts import render

# Create your views here. jan9
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework import authentication,permissions

from api.serializers import UserSerializer,ProductSerializer,BasketItemSerializer,BasketSerializer
from api.models import Product,BasketItem

class SignUpView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class ProductsView(viewsets.ModelViewSet):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()

    def create(self,request,*args,**kwargs):
        raise serializers.ValidationError('permission denied')
    def update(self,request,*args,**kwargs):
        raise serializers.ValidationError('permission denied')
    def destroy(self,request,*args,**kwargs):
        raise serializers.ValidationError('permission denied')
    
    #url:http://127.0.0.1:8000/api/products/{id}/add_to_basket/
    # method:post
    # jan 10
    @action(methods=['post'],detail=True)
    def add_to_basket(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        product_object=Product.objects.get(id=id)
        basket_object=request.user.cart
        serializer=BasketItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(product=product_object,basket=basket_object)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        

class BasketView(viewsets.ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permissionclasses=[permissions.IsAuthenticated]
    def list(self,request,*args,**kwargs):
        qs=request.user.cart #basket kitti
        serializer=BasketSerializer(qs,many=True)
        return Response(data=serializer.data)
    
class BasketItemView(viewsets.ModelViewSet):#jan 11
    serializer_class=BasketItemSerializer# modelviewset edukumbol ee fields venam
    queryset=BasketItem.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permissionclasses=[permissions.IsAuthenticated]

    def create(self,request,*args,**kwargs):
        raise serializers.ValidationError('permission denied')