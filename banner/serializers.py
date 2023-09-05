from rest_framework import serializers
from .models import Banner, Commercial, Slider


class BannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banner
        fields = '__all__'


class CommercialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Commercial
        fields = '__all__'


class SliderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slider
        fields = '__all__'
