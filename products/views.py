from django.shortcuts import render
from rest_framework import generics

from .models import Product
from .serializers import Productserializer


# generic create record
class ProductCreateApiView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = Productserializer

    # or we can send singnals instead
    def perform_create(self, serializer):
        # serializer.save(user = self.request.user)
        print(serializer.validated_data)
        tittle = serializer.validated_data.get('tittle')
        content = serializer.validated_data.get('content')
        if content is None:
            content=tittle
        serializer.save(content=content)
create_product_api = ProductCreateApiView.as_view()

# generic list vivew
class ProductListDeatilApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class=Productserializer

product_list_detail_view = ProductListDeatilApiView.as_view()
# class based api view
class ProductDeatilApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class=Productserializer

product_detail_view = ProductDeatilApiView.as_view()