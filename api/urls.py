from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_test),
    path('test1', views.api_test_2)
]