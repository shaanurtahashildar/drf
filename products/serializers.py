from rest_framework import serializers

from .models import Product
from .validators import validate_tittle_hello, unique_product_tittle


class Productserializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)

    # email=serializers.EmailField(write_only=True)
    tittle=serializers.CharField(validators=[validate_tittle_hello, unique_product_tittle])

    name =serializers.CharField(source='user.email', read_only=True)
    class Meta:
        model = Product
        fields = [
            'pk','tittle','name','content', 'price', 'sale_price', 'discount'
        ]

    # def validate_tittle(self, value):
    #     # qry= Product.objects.filter(tittle__exact=value)
    #     qry= Product.objects.filter(tittle__iexact=value)
    #     if qry.exists():
    #         raise serializers.ValidationError(f"{value} similar tittle already exist")
    #     return value
    # def create(self, validated_data):
    #     # return Product.objects.create(**validated_data)
    #     email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     print(obj, email)
    #     return obj

    def get_discount(self, obj):
        try:
            return obj.get_discount()
        except:
            return None