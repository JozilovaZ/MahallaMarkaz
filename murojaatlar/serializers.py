from rest_framework import serializers
from .models import Murojaat


class MurojaatSerializer(serializers.ModelSerializer):
    muallif_nomi = serializers.CharField(source='muallif.fullname', read_only=True)

    class Meta:
        model = Murojaat
        fields = '__all__'
        read_only_fields = ['muallif', 'mas_ul_user', 'holat', 'javob', 'yaratilgan', 'yangilangan']


class MurojaatAdminSerializer(serializers.ModelSerializer):
    muallif_nomi = serializers.CharField(source='muallif.fullname', read_only=True)

    class Meta:
        model = Murojaat
        fields = '__all__'
        read_only_fields = ['muallif', 'yaratilgan', 'yangilangan']
