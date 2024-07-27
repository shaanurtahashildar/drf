from rest_framework import serializers
from products.models import Product
from rest_framework.validators import UniqueValidator


# def validate_tittle( value):
#     # qry= Product.objects.filter(tittle__exact=value)
#     qry= Product.objects.filter(tittle__iexact=value)
#     if qry.exists():
#         raise serializers.ValidationError(f"{value} similar tittle already exist")
#     return value

def validate_tittle_hello(value):
    if 'hello' in value.lower():
        raise serializers.ValidationError("hello tittle not allowed")

unique_product_tittle = UniqueValidator(Product.objects.all())