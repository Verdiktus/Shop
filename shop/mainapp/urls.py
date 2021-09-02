from django.urls import path
from .views import test_view


urlpatterns = [
    path('', test_view, name='base')
    path('products/<str:ct_model>/<str:slug>/', view, name='product_detail')
]


