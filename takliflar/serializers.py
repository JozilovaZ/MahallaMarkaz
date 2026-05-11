from rest_framework import serializers
from .models import Taklif


class TaklifSerializer(serializers.ModelSerializer):
    muallif_nomi = serializers.CharField(source='muallif.fullname', read_only=True)

    class Meta:
        model = Taklif
        fields = '__all__'
        read_only_fields = ['muallif', 'ko_rib_chiqildi', 'yaratilgan']
