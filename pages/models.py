from django.db import models
from django.conf import settings
from django.utils import timezone


class MahallaInfo(models.Model):
    tuman = models.CharField(max_length=100)
    mahalla = models.CharField(max_length=100)
    manzil = models.CharField(max_length=200, blank=True)
    telefon = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    class Meta:
        verbose_name = "Mahalla ma'lumoti"

    def __str__(self):
        return f"{self.mahalla}, {self.tuman}"


class MahallaRahbar(models.Model):
    LAVOZIM_CHOICES = [
        ('rais', 'Mahalla raisi'),
        ('hokim_yordamchisi', 'Hokim yordamchisi'),
        ('yoshlar', 'Yoshlar yetakchisi'),
        ('xotin_qizlar', 'Xotin-qizlar'),
        ('profilaktika', 'Profilaktika inspektori'),
        ('boshqa', 'Boshqa'),
    ]

    ismi = models.CharField(max_length=150)
    lavozim = models.CharField(max_length=30, choices=LAVOZIM_CHOICES)
    lavozim_tavsifi = models.CharField(max_length=200, blank=True)
    telefon = models.CharField(max_length=20, blank=True)
    tartib = models.IntegerField(default=0)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='rahbar_profil'
    )

    class Meta:
        ordering = ['tartib']

    def __str__(self):
        return f"{self.ismi} - {self.get_lavozim_display()}"


class RahbarXabar(models.Model):
    HOLAT_CHOICES = [
        ('kutilmoqda', 'Kutilmoqda'),
        ('tasdiqlangan', 'Tasdiqlangan'),
        ('bekor_qilingan', 'Bekor qilingan'),
    ]

    rahbar = models.ForeignKey(MahallaRahbar, on_delete=models.CASCADE, related_name='xabarlar')
    yuboruvchi_ism = models.CharField(max_length=150)
    yuboruvchi_telefon = models.CharField(max_length=20, blank=True)
    matn = models.TextField()
    javob = models.TextField(blank=True)
    holat = models.CharField(max_length=20, choices=HOLAT_CHOICES, default='kutilmoqda')
    yuborilgan_vaqt = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-yuborilgan_vaqt']
        verbose_name = "Rahbarga xabar"

    def __str__(self):
        return f"{self.yuboruvchi_ism} - {self.rahbar.ismi}: {self.matn[:40]}"
