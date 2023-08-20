from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class ShoppingItem(models.Model):
    categories = [
        ('electronics', 'Electronics'),
        ('clothing', 'Clothing'),
        ('pharmacy', 'Pharmacy'),
        ('beauty', 'Beauty'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=categories)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    discount = models.DecimalField(max_digits=5,default=0, decimal_places=2,
                                   validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return str(self.name) + '_' + str(self.category)