from django.urls import path
from .  import views
from .views import product_detail_view, create_product_api, product_list_detail_view, product_alt_view

urlpatterns = [
    path("<int:pk>/", views.ProductDeatilApiView.as_view()),
    path("", create_product_api),
    path("list/", product_list_detail_view),
    path("<int:pk>/", product_detail_view),
    # path("", views.product_alt_view),
    # path("list/", views.product_alt_view),
    # path("<int:pk>/", views.product_alt_view),
    # path("<int:pk>/update", views.product_update_view),
    # path("<int:pk>/delete", views.product_destroy_view),

    # mixin view
    path("mixin/", views.product_mixin_view),
    path("mixin/<int:pk>/", views.product_mixin_view),
]