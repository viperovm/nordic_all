from rest_framework import serializers
from .models import FaqElement, ExtraElement


class FaqElementSerializer(serializers.ModelSerializer):

    class Meta:
        model = FaqElement
        fields = '__all__'


class ExtraElementSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExtraElement
        fields = '__all__'
