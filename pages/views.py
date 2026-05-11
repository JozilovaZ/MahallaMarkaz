from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import MahallaInfo, MahallaRahbar, RahbarXabar
from .serializers import MahallaInfoSerializer, MahallaRahbarSerializer, RahbarXabarSerializer


def main(request):
    return redirect('/login/')

def login_page(request):
    return render(request, 'login.html')

@login_required(login_url='/login/')
def murojaat(request):
    return render(request, 'murojaat.html')

@login_required(login_url='/login/')
def taklif(request):
    return render(request, 'taklif.html')

@login_required(login_url='/login/')
def mxizmatlari(request):
    return render(request, 'mxizmatlari.html')

@login_required(login_url='/login/')
def pasport(request):
    return render(request, 'pasport.html')

@login_required(login_url='/login/')
def admin_panel(request):
    return render(request, 'admin_panel.html')

@login_required(login_url='/login/')
def admin_users(request):
    return render(request, 'admin_users.html')

@login_required(login_url='/login/')
def admin_login(request):
    return render(request, 'admin_login.html')

@login_required(login_url='/login/')
def rahbar_profil(request, pk):
    return render(request, 'rahbar-profil.html')

@login_required(login_url='/login/')
def mas_ul_kabinet(request):
    return render(request, 'mas-ul-kabinet.html')

@login_required(login_url='/login/')
def admin_xabarlar(request):
    return render(request, 'admin_xabarlar.html')


class MahallaInfoView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        info = MahallaInfo.objects.first()
        if not info:
            return Response({})
        return Response(MahallaInfoSerializer(info).data)

    def put(self, request):
        info = MahallaInfo.objects.first()
        if not info:
            serializer = MahallaInfoSerializer(data=request.data)
        else:
            serializer = MahallaInfoSerializer(info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]


class MahallaRahbarListView(generics.ListCreateAPIView):
    queryset = MahallaRahbar.objects.all()
    serializer_class = MahallaRahbarSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]


class MahallaRahbarDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MahallaRahbar.objects.all()
    serializer_class = MahallaRahbarSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]


class RahbarXabarView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, pk):
        try:
            rahbar = MahallaRahbar.objects.get(pk=pk)
        except MahallaRahbar.DoesNotExist:
            return Response({'detail': 'Rahbar topilmadi'}, status=status.HTTP_404_NOT_FOUND)
        data = request.data.copy()
        data['rahbar'] = pk
        serializer = RahbarXabarSerializer(data=data)
        if serializer.is_valid():
            xabar = serializer.save()
            return Response({'detail': 'Xabar muvaffaqiyatli yuborildi!', 'id': xabar.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        xabarlar = RahbarXabar.objects.filter(rahbar_id=pk)
        serializer = RahbarXabarSerializer(xabarlar, many=True)
        return Response(serializer.data)


class XabarlarOmmaviyView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        tasdiqlangan = RahbarXabar.objects.filter(holat='tasdiqlangan').count()
        return Response({'tasdiqlangan': tasdiqlangan})


class AdminXabarlarView(generics.ListAPIView):
    queryset = RahbarXabar.objects.all().order_by('-yuborilgan_vaqt')
    serializer_class = RahbarXabarSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        if not (user.is_staff or getattr(user, 'role', None) == 'admin'):
            return Response({'detail': 'Ruxsat yo\'q'}, status=status.HTTP_403_FORBIDDEN)
        return super().get(request, *args, **kwargs)


class MenингXabarlarim(APIView):
    """Mas'ul shaxs o'z xabarlarini ko'radi va boshqaradi."""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            rahbar = request.user.rahbar_profil
        except MahallaRahbar.DoesNotExist:
            return Response({'detail': "Sizning rahbar profilingiz topilmadi"}, status=403)
        xabarlar = RahbarXabar.objects.filter(rahbar=rahbar)
        serializer = RahbarXabarSerializer(xabarlar, many=True)
        return Response(serializer.data)


class XabarHolatView(APIView):
    """Mas'ul shaxs xabarni tasdiqlaydi yoki bekor qiladi."""
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        try:
            rahbar = request.user.rahbar_profil
        except Exception:
            return Response({'detail': "Rahbar profili topilmadi"}, status=403)
        try:
            xabar = RahbarXabar.objects.get(pk=pk, rahbar=rahbar)
        except RahbarXabar.DoesNotExist:
            return Response({'detail': "Xabar topilmadi yoki ruxsat yo'q"}, status=404)

        holat = request.data.get('holat')
        if holat not in ('tasdiqlangan', 'bekor_qilingan'):
            return Response({'detail': "holat: 'tasdiqlangan' yoki 'bekor_qilingan' bo'lishi kerak"}, status=400)

        xabar.holat = holat
        xabar.javob = request.data.get('javob', '')
        xabar.save()
        return Response(RahbarXabarSerializer(xabar).data)
