from .models import ShoppingItem
from rest_framework import serializers


class ShoppingItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoppingItem
        fields = ['name', 'category', 'discount', 'price']
