from django.shortcuts import render, get_object_or_404
from rest_framework import generics,  mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
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

# update
class ProductUpdatelApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class=Productserializer
    lookup_field = "pk"
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.tittle

product_update_view = ProductUpdatelApiView.as_view()

# delete records
class ProductDestroylApiView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class=Productserializer
    lookup_field = "pk"
    def perform_destroy(self, intance):
        super().perform_destroy(intance)

product_destroy_view = ProductDestroylApiView.as_view()
# function based api view
@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    # breakpoint()
    if method == "GET" :
        if pk is not None:
            # return only respective records
            obj = get_object_or_404(Product, pk = pk)
            data = Productserializer(obj, many=False).data
            return Response(data)
        # return all records
        queryset =Product.objects.all()
        data=Productserializer(queryset, many=True).data
        return Response(data)
    if method == "POST":
        serializer = Productserializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            tittle = serializer.validated_data.get('tittle')
            content = serializer.validated_data.get('content')
            if content is None:
                content = tittle
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"details: invalid data"}, status=400)




# class based views
class ProductMixinView(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class =Productserializer
    # lookup_field = "pk"
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def perform_create(self, serializer):
        # serializer.save(user = self.request.user)
        tittle = serializer.validated_data.get('tittle')
        content = serializer.validated_data.get('content')
        if content is None:
            content="this is mixin addedcontent"
        serializer.save(content=content)
product_mixin_view = ProductMixinView.as_view()