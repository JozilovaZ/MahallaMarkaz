from django.urls import path
from . import views

urlpatterns = [
    path('elonlar/', views.ElonListCreateView.as_view(), name='elon-list'),
    path('elonlar/<int:pk>/', views.ElonDetailView.as_view(), name='elon-detail'),
    path('ishlar/', views.IshOrniListCreateView.as_view(), name='ish-list'),
    path('ishlar/<int:pk>/', views.IshOrniDetailView.as_view(), name='ish-detail'),
]
