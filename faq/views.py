from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import FaqElement, ExtraElement
from .serializers import FaqElementSerializer, ExtraElementSerializer


class FaqElementViewSet(viewsets.ModelViewSet):
    queryset = FaqElement.objects.all()
    serializer_class = FaqElementSerializer
    permission_classes = [AllowAny]


class ExtraElementViewSet(viewsets.ModelViewSet):
    queryset = ExtraElement.objects.all()
    serializer_class = ExtraElementSerializer
    permission_classes = [AllowAny]
