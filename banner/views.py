from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Banner, Commercial, Slider
from .serializers import BannerSerializer, CommercialSerializer, SliderSerializer


class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.filter(is_active=True)
    serializer_class = BannerSerializer
    permission_classes = [AllowAny]


class CommercialViewSet(viewsets.ModelViewSet):
    queryset = Commercial.objects.filter(is_active=True)
    serializer_class = CommercialSerializer
    permission_classes = [AllowAny]


class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.filter(is_active=True)
    serializer_class = SliderSerializer
    permission_classes = [AllowAny]

