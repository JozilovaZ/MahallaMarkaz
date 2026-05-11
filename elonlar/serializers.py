from rest_framework import serializers
from .models import Elon, IshOrni


class ElonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elon
        fields = '__all__'
        read_only_fields = ['yaratilgan']


class IshOrniSerializer(serializers.ModelSerializer):
    class Meta:
        model = IshOrni
        fields = '__all__'
        read_only_fields = ['yaratilgan']
