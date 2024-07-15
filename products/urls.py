from django.urls import path
from .  import views
from .views import product_detail_view, create_product_api, product_list_detail_view

urlpatterns = [
    # path("<int:pk>/", views.ProductDeatilApiView.as_view())
    path("", create_product_api),
    path("list/", product_list_detail_view),
    path("<int:pk>/", product_detail_view)
]