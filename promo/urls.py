from django.urls import path
from .views import promo_view


urlpatterns = [
    path('promo/', promo_view, name='promo_view'),
]
