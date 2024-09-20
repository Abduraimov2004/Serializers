from django.urls import path, include
from .views import home, products, category

urlpatterns = [

    path('', home),
    path('products', products),
    path('category', category, name='bolim'),
]
