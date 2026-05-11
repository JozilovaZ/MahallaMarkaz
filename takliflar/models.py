from django.db import models
from django.conf import settings


class Taklif(models.Model):
    PRIORITY_CHOICES = [
        ('past', 'Past'),
        ('orta', "O'rta"),
        ('yuqori', 'Yuqori'),
        ('shoshilinch', 'Shoshilinch'),
    ]

    CATEGORY_CHOICES = [
        ('infratuzilma', 'Infratuzilma'),
        ('xavfsizlik', 'Xavfsizlik'),
        ('ekologiya', 'Ekologiya'),
        ('ijtimoiy', 'Ijtimoiy'),
        ('madaniy', 'Madaniy'),
        ('boshqa', 'Boshqa'),
    ]

    muallif = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='takliflar')
    sarlavha = models.CharField(max_length=200)
    kategoriya = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='boshqa')
    ustuvorlik = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='orta')
    mazmun = models.TextField()
    ko_rib_chiqildi = models.BooleanField(default=False)
    yaratilgan = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-yaratilgan']

    def __str__(self):
        return self.sarlavha
