from django.core.management.base import BaseCommand
from pages.models import MahallaInfo, MahallaRahbar
from elonlar.models import Elon, IshOrni
from datetime import date, timedelta


class Command(BaseCommand):
    help = "Namuna ma'lumotlar kiritish"

    def handle(self, *args, **options):
        # MahallaInfo
        if not MahallaInfo.objects.exists():
            MahallaInfo.objects.create(
                tuman="Yunusobod",
                mahalla="Yangi Hayot",
                manzil="Toshkent sh., Yunusobod t., Yangi Hayot ko'chasi, 12",
                telefon="+998 71 234 56 78",
                email="yangi.hayot@mahalla.uz",
            )
            self.stdout.write(self.style.SUCCESS("MahallaInfo yaratildi"))

        # Rahbarlar
        if not MahallaRahbar.objects.exists():
            rahbarlar = [
                dict(ismi="Berdiyev Bektamish Qazaqovich", lavozim="rais",
                     lavozim_tavsifi="Mahalla raisi — mahalla boshlig'i",
                     telefon="+998 90 111 22 33", tartib=1),
                dict(ismi="Xudoyorov Muhammadjon Iris o'g'li", lavozim="hokim_yordamchisi",
                     lavozim_tavsifi="Hokim yordamchisi — tuman hokimligi vakili",
                     telefon="+998 90 222 33 44", tartib=2),
                dict(ismi="Usmonov Bekzod Mashrabjon o'g'li", lavozim="yoshlar",
                     lavozim_tavsifi="Yoshlar yetakchisi — yoshlar ishlari bo'yicha",
                     telefon="+998 90 333 44 55", tartib=3),
                dict(ismi="Maxkamova Zamiraxon Tillovoldiyevna", lavozim="xotin_qizlar",
                     lavozim_tavsifi="Xotin-qizlar masalalari bo'yicha mas'ul",
                     telefon="+998 90 444 55 66", tartib=4),
                dict(ismi="Muxammadiyev Sarvarjon Nasimovich", lavozim="profilaktika",
                     lavozim_tavsifi="Profilaktika inspektori — huquqni muhofaza qilish",
                     telefon="+998 90 555 66 77", tartib=5),
            ]
            for r in rahbarlar:
                MahallaRahbar.objects.create(**r)
            self.stdout.write(self.style.SUCCESS(f"{len(rahbarlar)} ta rahbar yaratildi"))

        # Elonlar
        if not Elon.objects.exists():
            elonlar = [
                dict(sarlavha="Ko'cha yoritgichlari ta'mirlash ishlari",
                     mazmun="2026-yil 10-may kuni mahallaning asosiy ko'chalarida yoritgichlar ta'mirlanadi. Aholidan chiqish yo'llarini bo'shatib qo'yish so'raladi.",
                     sana=date.today() + timedelta(days=6)),
                dict(sarlavha="Umumiy yig'ilish chaqirilmoqda",
                     mazmun="2026-yil 12-may kuni soat 10:00 da mahalla markazida umumiy yig'ilish o'tkaziladi. Barcha uy egalari ishtirok etishlari shart.",
                     sana=date.today() + timedelta(days=8)),
                dict(sarlavha="Sanitariya kuni e'lon qilinadi",
                     mazmun="Har shanba kuni ertalab 08:00-10:00 soatlar oralig'ida umumiy tozalash ishlari olib boriladi. Barcha ko'cha-ko'y va hovlilarni tozalash tavsiya etiladi.",
                     sana=date.today() + timedelta(days=3)),
                dict(sarlavha="Bolalar bog'chasiga qabul",
                     mazmun="2026-2027 o'quv yili uchun bolalar bog'chasiga 3-6 yoshli bolalar qabul qilinmoqda. Hujjatlarni mahalla ma'muriyatiga topshiring.",
                     sana=date.today() + timedelta(days=14)),
                dict(sarlavha="Suv ta'minoti vaqtincha to'xtatiladi",
                     mazmun="2026-yil 7-may kuni soat 09:00-15:00 oralig'ida texnik ishlar sababli suv ta'minoti vaqtincha to'xtatiladi.",
                     sana=date.today() + timedelta(days=3)),
            ]
            for e in elonlar:
                Elon.objects.create(**e)
            self.stdout.write(self.style.SUCCESS(f"{len(elonlar)} ta e'lon yaratildi"))

        # Ish o'rinlari
        if not IshOrni.objects.exists():
            ishlar = [
                dict(sarlavha="Mahalla kotibiyati xodimi",
                     mazmun="Hujjatlar bilan ishlash, ariza va murojaatlarni qayta ishlash. Talab: yuqori ma'lumot, kompyuter savodxonligi. Ish haqi: muzokaraga asosan.",
                     muddat=date.today() + timedelta(days=30)),
                dict(sarlavha="Bog'bon — ko'kalamzorlashtirish",
                     mazmun="Mahalla hududidagi daraxtlar, gullar va maysazorlarni parvarish qilish. Tajriba talab qilinmaydi. Ish haqi: 1,800,000 so'm/oy.",
                     muddat=date.today() + timedelta(days=20)),
                dict(sarlavha="Sanitariya inspektori yordamchisi",
                     mazmun="Mahalla hududida sanitariya nazoratini olib borish, hisobotlar tuzish. Talab: tibbiyot yoki ekologiya sohasida ma'lumot.",
                     muddat=date.today() + timedelta(days=25)),
                dict(sarlavha="IT mutaxassisi (yarim stavka)",
                     mazmun="Mahalla axborot tizimini yuritish, veb-saytni qo'llab-quvvatlash. Talab: veb texnologiyalari bilimi. Ish haqi: 1,500,000 so'm/oy.",
                     muddat=date.today() + timedelta(days=15)),
            ]
            for i in ishlar:
                IshOrni.objects.create(**i)
            self.stdout.write(self.style.SUCCESS(f"{len(ishlar)} ta ish o'rni yaratildi"))

        self.stdout.write(self.style.SUCCESS("Barcha ma'lumotlar muvaffaqiyatli kiritildi!"))
