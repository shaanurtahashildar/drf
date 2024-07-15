import json

from django.contrib.sites import requests
from django.forms import model_to_dict
from django.http import JsonResponse
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import Productserializer


@api_view(["POST"])
def api_test_2(request, *args, **kwargs):
    serializer = Productserializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance=serializer.save()
        print(instance)
        return Response(serializer.data)
    return {"response" : "invalid data"}

    # if request.GET:
    #     res = Product.objects.all().order_by("?").first()
    #     data={}
    #     if res:
    #         # data=model_to_dict(res, fields=['id', 'tittle', 'sale_price'])
    #         data = Productserializer(res).data
    #     return Response(data)
def api_test(request, *args, **kwargs):
    body = request.body
    data={}
    try :
         data=json.loads(body)
    except :
        pass
    data["params"] = dict(request.GET)
    data["headers"] = dict(request.headers)
    return JsonResponse(data)


