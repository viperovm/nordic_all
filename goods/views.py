from django.db.models.query import Prefetch
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from .models import Goods, GoodsCategory, GoodsSize
from .serializers import GoodsSerializer, CategorySerializer, SizeSerializer


# @api_view()
# @permission_classes((permissions.AllowAny,))
# def goods_view(request):
#     goods = Goods.objects.all()
#     serializer = GoodsSerializer(goods, context={'request': request})
#     return Response(serializer.data)


class GoodsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    permission_classes = [AllowAny]


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GoodsCategory.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class SizeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GoodsSize.objects.all()
    serializer_class = SizeSerializer
    permission_classes = [AllowAny]
