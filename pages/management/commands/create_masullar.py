from django.core.management.base import BaseCommand
from accounts.models import User
from pages.models import MahallaRahbar


MASULLAR = [
    dict(ismi="Berdiyev Bektamish Qazaqovich",   lavozim="rais",             email="rais@mahalla.uz",       password="Mahalla@2026"),
    dict(ismi="Xudoyorov Muhammadjon Iris o'g'li", lavozim="hokim_yordamchisi", email="hokim@mahalla.uz",      password="Mahalla@2026"),
    dict(ismi="Usmonov Bekzod Mashrabjon o'g'li",  lavozim="yoshlar",          email="yoshlar@mahalla.uz",    password="Mahalla@2026"),
    dict(ismi="Maxkamova Zamiraxon Tillovoldiyevna", lavozim="xotin_qizlar",   email="xotinqizlar@mahalla.uz", password="Mahalla@2026"),
    dict(ismi="Muxammadiyev Sarvarjon Nasimovich",  lavozim="profilaktika",    email="profilaktika@mahalla.uz", password="Mahalla@2026"),
]


class Command(BaseCommand):
    help = "Mas'ul shaxslar uchun foydalanuvchilar yaratish"

    def handle(self, *args, **options):
        for m in MASULLAR:
            user, created = User.objects.get_or_create(
                email=m['email'],
                defaults=dict(fullname=m['ismi'], role='responsible')
            )
            if created:
                user.set_password(m['password'])
                user.save()

            try:
                rahbar = MahallaRahbar.objects.get(lavozim=m['lavozim'])
                rahbar.user = user
                rahbar.save()
            except MahallaRahbar.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"Rahbar topilmadi: {m['lavozim']}"))

            status = "YANGI" if created else "MAVJUD"
            self.stdout.write(f"[{status}] {m['ismi']}")
            self.stdout.write(f"        Email   : {m['email']}")
            self.stdout.write(f"        Parol   : {m['password']}")
            self.stdout.write("")

        self.stdout.write(self.style.SUCCESS("Barcha mas'ullar tayyor!"))
