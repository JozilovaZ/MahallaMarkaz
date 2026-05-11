from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from pages.models import MahallaRahbar
from .models import Murojaat
from .serializers import MurojaatSerializer, MurojaatAdminSerializer


class MurojaatListCreateView(generics.ListCreateAPIView):
    serializer_class = MurojaatSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.role == 'admin':
            return Murojaat.objects.all()
        if user.role == 'responsible':
            return Murojaat.objects.filter(mas_ul_user=user)
        return Murojaat.objects.filter(muallif=user)

    def perform_create(self, serializer):
        user = self.request.user
        rahbar_id = self.request.data.get('rahbar_id')
        mas_ul_user = None
        if rahbar_id:
            try:
                rahbar = MahallaRahbar.objects.get(pk=rahbar_id)
                mas_ul_user = rahbar.user
            except MahallaRahbar.DoesNotExist:
                pass
        serializer.save(
            muallif=user,
            mas_ul_user=mas_ul_user,
            fullname=user.fullname or '',
            phone=user.phone or '',
        )


class MurojaatDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.role == 'admin':
            return Murojaat.objects.all()
        return Murojaat.objects.filter(muallif=user)

    def get_serializer_class(self):
        user = self.request.user
        if user.is_staff or user.role == 'admin':
            return MurojaatAdminSerializer
        return MurojaatSerializer


class MurojaatStatsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.is_staff or user.role == 'admin':
            qs = Murojaat.objects.all()
        else:
            qs = Murojaat.objects.filter(muallif=user)

        return Response({
            'jami': qs.count(),
            'yuborildi': qs.filter(holat='yuborildi').count(),
            'jarayonda': qs.filter(holat='jarayonda').count(),
            'bajarildi': qs.filter(holat='bajarildi').count(),
            'rad_etildi': qs.filter(holat='rad_etildi').count(),
        })
