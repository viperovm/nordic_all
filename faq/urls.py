from rest_framework.routers import DefaultRouter
from .views import FaqElementViewSet, ExtraElementViewSet


router = DefaultRouter()
router.register(r'faq', FaqElementViewSet, basename='faq')
router.register(r'extra', ExtraElementViewSet, basename='extra')

urlpatterns = [
#     # path('infofororders/<pk>/', InfoForOrderView.as_view()),
#     path('goods/', goods_view, name='goods_view'),
]

urlpatterns += router.urls