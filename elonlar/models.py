from django.db import models


class Elon(models.Model):
    sarlavha = models.CharField(max_length=200)
    mazmun = models.TextField()
    sana = models.DateField()
    faol = models.BooleanField(default=True)
    yaratilgan = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-sana']

    def __str__(self):
        return self.sarlavha


class IshOrni(models.Model):
    sarlavha = models.CharField(max_length=200)
    mazmun = models.TextField()
    muddat = models.DateField()
    faol = models.BooleanField(default=True)
    yaratilgan = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-yaratilgan']

    def __str__(self):
        return self.sarlavha
