from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import OrdersViewSet


router = DefaultRouter()
router.register(r'orders', OrdersViewSet, basename='orders')

urlpatterns = [
    # path('promo/', promo_view, name='promo_view'),
]

urlpatterns += router.urls