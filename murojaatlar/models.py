from django.db import models
from django.conf import settings


class Murojaat(models.Model):
    STATUS_CHOICES = [
        ('yuborildi', 'Yuborildi'),
        ('jarayonda', 'Jarayonda'),
        ('bajarildi', 'Bajarildi'),
        ('rad_etildi', "Rad etildi"),
    ]

    CATEGORY_CHOICES = [
        ('kommunal', 'Kommunal xizmatlar'),
        ('yol', "Yo'l va ko'cha"),
        ('xavfsizlik', 'Xavfsizlik'),
        ('sanitariya', 'Sanitariya va ekologiya'),
        ('ijtimoiy', 'Ijtimoiy yordam'),
        ('boshqa', 'Boshqa'),
    ]

    muallif = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='murojaatlar')
    mas_ul_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='keladigan_murojaatlar'
    )
    fullname = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    mavzu = models.CharField(max_length=200)
    kategoriya = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='boshqa')
    mas_ul = models.CharField(max_length=150, blank=True)
    mazmun = models.TextField()
    holat = models.CharField(max_length=20, choices=STATUS_CHOICES, default='yuborildi')
    javob = models.TextField(blank=True)
    yaratilgan = models.DateTimeField(auto_now_add=True)
    yangilangan = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-yaratilgan']

    def __str__(self):
        return f'{self.mavzu} - {self.holat}'
