from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .models import Elon, IshOrni
from .serializers import ElonSerializer, IshOrniSerializer


class ElonListCreateView(generics.ListCreateAPIView):
    queryset = Elon.objects.filter(faol=True)
    serializer_class = ElonSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]


class ElonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Elon.objects.all()
    serializer_class = ElonSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]


class IshOrniListCreateView(generics.ListCreateAPIView):
    queryset = IshOrni.objects.filter(faol=True)
    serializer_class = IshOrniSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]


class IshOrniDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IshOrni.objects.all()
    serializer_class = IshOrniSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]
