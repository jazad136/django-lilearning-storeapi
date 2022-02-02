
from rest_framework import serializers

from store.models import Product, ShoppingCartItem

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCartItem
        fields = ('product', 'quantity')

class ProductSerializer(serializers.ModelSerializer):
    is_on_sale = serializers.BooleanField(read_only=True)
    current_price = serializers.FloatField(read_only=True)
    description = serializers.CharField(min_length=2, max_length=200)
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'sale_start', 'sale_end'
        ,'is_on_sale', 'current_price', 'cart_items'
        )
    
    def get_cart_items(self, instance):
        items = ShoppingCartItem.objects.filter(product=instance)
        

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['is_on_sale'] = instance.is_on_sale()
    #     data['current_price'] = instance.current_price()
    #     return data

