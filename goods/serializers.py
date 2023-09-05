from rest_framework import serializers
from .models import Goods, GoodsImages, GoodsCategory, GoodsSize


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsSize
        fields = '__all__'


class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImages
        fields = '__all__'


class GoodsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    price = serializers.CharField(read_only=True)
    goods_gallery = GoodsImageSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True, many=False)
    size = SizeSerializer(read_only=True, many=True)
    description = serializers.CharField(read_only=True)

    class Meta:
        model = Goods
        fields = '__all__'

