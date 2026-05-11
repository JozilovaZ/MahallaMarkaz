from django.contrib import admin
from .models import Taklif


@admin.register(Taklif)
class TaklifAdmin(admin.ModelAdmin):
    list_display = ['sarlavha', 'muallif', 'kategoriya', 'ustuvorlik', 'ko_rib_chiqildi', 'yaratilgan']
    list_filter = ['kategoriya', 'ustuvorlik', 'ko_rib_chiqildi']
    list_editable = ['ko_rib_chiqildi']
