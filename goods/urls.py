from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import GoodsViewSet, CategoryViewSet, SizeViewSet


router = DefaultRouter()
router.register(r'goods', GoodsViewSet, basename='goods')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'sizes', SizeViewSet, basename='sizes')

urlpatterns = [
#     # path('infofororders/<pk>/', InfoForOrderView.as_view()),
#     path('goods/', goods_view, name='goods_view'),
]

urlpatterns += router.urls