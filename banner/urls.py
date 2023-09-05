from rest_framework.routers import DefaultRouter
from .views import BannerViewSet, CommercialViewSet, SliderViewSet


router = DefaultRouter()
router.register(r'banner', BannerViewSet, basename='banner')
router.register(r'commercial', CommercialViewSet, basename='commercial')
router.register(r'slider', SliderViewSet, basename='slider')

urlpatterns = [
#     # path('infofororders/<pk>/', InfoForOrderView.as_view()),
#     path('goods/', goods_view, name='goods_view'),
]

urlpatterns += router.urls