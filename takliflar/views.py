from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Taklif
from .serializers import TaklifSerializer


class TaklifListCreateView(generics.ListCreateAPIView):
    serializer_class = TaklifSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.role == 'admin':
            return Taklif.objects.all()
        return Taklif.objects.filter(muallif=user)

    def perform_create(self, serializer):
        serializer.save(muallif=self.request.user)


class TaklifDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaklifSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.role == 'admin':
            return Taklif.objects.all()
        return Taklif.objects.filter(muallif=user)
