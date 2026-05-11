from django.contrib import admin
from .models import Elon, IshOrni


@admin.register(Elon)
class ElonAdmin(admin.ModelAdmin):
    list_display = ['sarlavha', 'sana', 'faol', 'yaratilgan']
    list_editable = ['faol']


@admin.register(IshOrni)
class IshOrniAdmin(admin.ModelAdmin):
    list_display = ['sarlavha', 'muddat', 'faol', 'yaratilgan']
    list_editable = ['faol']
