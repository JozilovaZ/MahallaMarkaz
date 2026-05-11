from django.contrib import admin
from .models import Murojaat


@admin.register(Murojaat)
class MurojaatAdmin(admin.ModelAdmin):
    list_display = ['mavzu', 'muallif', 'kategoriya', 'holat', 'yaratilgan']
    list_filter = ['holat', 'kategoriya']
    search_fields = ['mavzu', 'fullname', 'phone']
    list_editable = ['holat']
