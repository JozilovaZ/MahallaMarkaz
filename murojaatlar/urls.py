from django.urls import path
from . import views

urlpatterns = [
    path('', views.MurojaatListCreateView.as_view(), name='murojaat-list'),
    path('stats/', views.MurojaatStatsView.as_view(), name='murojaat-stats'),
    path('<int:pk>/', views.MurojaatDetailView.as_view(), name='murojaat-detail'),
]
