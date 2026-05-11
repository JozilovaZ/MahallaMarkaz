from django.contrib import admin
from .models import MahallaInfo, MahallaRahbar, RahbarXabar


@admin.register(MahallaInfo)
class MahallaInfoAdmin(admin.ModelAdmin):
    list_display = ['mahalla', 'tuman', 'telefon']


@admin.register(MahallaRahbar)
class MahallaRahbarAdmin(admin.ModelAdmin):
    list_display = ['ismi', 'lavozim', 'telefon', 'tartib']


@admin.register(RahbarXabar)
class RahbarXabarAdmin(admin.ModelAdmin):
    list_display = ['rahbar', 'yuboruvchi_ism', 'yuboruvchi_telefon', 'yuborilgan_vaqt', 'holat']
    list_filter = ['holat', 'rahbar']
    list_editable = ['holat']
