from django import forms
from .models import ShoppingItem


class ShopForm(forms.ModelForm):
    class Meta:
        model = ShoppingItem
        fields = ['name', 'category', 'price', 'discount']