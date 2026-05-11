from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login_page, name='login'),
    path('xizmatlar/', views.mxizmatlari, name='xizmatlar'),
    path('murojaat/', views.murojaat, name='murojaat'),
    path('taklif/', views.taklif, name='taklif'),
    path('pasport/', views.pasport, name='pasport'),
    path('kabinet/', views.mas_ul_kabinet, name='mas_ul_kabinet'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('admin-panel/xabarlar/', views.admin_xabarlar, name='admin_xabarlar'),
    path('admin-foydalanuvchilar/', views.admin_users, name='admin_users'),
    path('admin-kirish/', views.admin_login, name='admin_login'),
    path('rahbar/<int:pk>/', views.rahbar_profil, name='rahbar_profil'),
]

api_urlpatterns = [
    path('mahalla-info/', views.MahallaInfoView.as_view(), name='mahalla_info'),
    path('xabarlar-ommaviy/', views.XabarlarOmmaviyView.as_view(), name='xabarlar_ommaviy'),
    path('rahbarlar/', views.MahallaRahbarListView.as_view(), name='rahbarlar_list'),
    path('rahbarlar/<int:pk>/', views.MahallaRahbarDetailView.as_view(), name='rahbar_detail'),
    path('rahbarlar/<int:pk>/xabar/', views.RahbarXabarView.as_view(), name='rahbar_xabar'),
    path('xabarlar/', views.AdminXabarlarView.as_view(), name='xabarlar_list'),
    path('mening-xabarlarim/', views.MenингXabarlarim.as_view(), name='mening_xabarlarim'),
    path('xabarlar/<int:pk>/holat/', views.XabarHolatView.as_view(), name='xabar_holat'),
]
