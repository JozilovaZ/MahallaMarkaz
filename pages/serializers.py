from rest_framework import serializers
from .models import MahallaInfo, MahallaRahbar, RahbarXabar


class MahallaInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MahallaInfo
        fields = '__all__'


class MahallaRahbarSerializer(serializers.ModelSerializer):
    lavozim_display = serializers.CharField(source='get_lavozim_display', read_only=True)
    xabarlar_soni = serializers.SerializerMethodField()

    class Meta:
        model = MahallaRahbar
        fields = '__all__'

    def get_xabarlar_soni(self, obj):
        return obj.xabarlar.filter(holat='kutilmoqda').count()


class RahbarXabarSerializer(serializers.ModelSerializer):
    rahbar_ismi = serializers.CharField(source='rahbar.ismi', read_only=True)
    rahbar_lavozim = serializers.CharField(source='rahbar.get_lavozim_display', read_only=True)
    holat_display = serializers.CharField(source='get_holat_display', read_only=True)

    class Meta:
        model = RahbarXabar
        fields = ['id', 'rahbar', 'rahbar_ismi', 'rahbar_lavozim',
                  'yuboruvchi_ism', 'yuboruvchi_telefon', 'matn',
                  'javob', 'holat', 'holat_display', 'yuborilgan_vaqt']
        read_only_fields = ['id', 'yuborilgan_vaqt']
