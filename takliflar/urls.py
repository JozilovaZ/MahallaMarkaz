from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaklifListCreateView.as_view(), name='taklif-list'),
    path('<int:pk>/', views.TaklifDetailView.as_view(), name='taklif-detail'),
]
