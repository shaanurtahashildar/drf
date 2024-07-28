from rest_framework import serializers

# from products.models import Product


class UserPublicserializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    data = []

# class Productserializer(serializers.ModelSerializer):
#     discount = serializers.SerializerMethodField(read_only=True)
#     class Meta:
#         model = Product
#         fields = [
#             'id','tittle', 'price', 'sale_price', 'discount'
#         ]
#     def get_discount(self, obj):
#         try:
#             return obj.get_discount()
#         except:
#             return None