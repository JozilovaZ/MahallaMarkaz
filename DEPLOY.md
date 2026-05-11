# Serverga yuklash yo'riqnomasi

## 1. Serverga loyihani yuklash

```bash
git clone <repo-url> /home/mahalla
cd /home/mahalla
```

Yoki fayllarni SCP bilan yuborish:
```bash
scp -r ./MahallaLoyiha user@server-ip:/home/mahalla
```

## 2. .env fayl yaratish

```bash
cp .env.example .env
nano .env
```

`.env` ichida:
```
DJANGO_SECRET_KEY=yangi-uzun-tasodifiy-kalit-yozing
```

## 3. Localdan ma'lumotlar bazasini serverga ko'chirish

```bash
# Localdan serverga db.sqlite3 yuborish
scp db.sqlite3 user@server-ip:/home/mahalla/

# Server tomonida volume'ga ko'chirish (konteyner ishlagandan keyin)
docker cp db.sqlite3 mahalla_web:/app/db.sqlite3
```

## 4. Docker bilan ishga tushirish

```bash
docker compose up -d --build
```

## 5. Konteyner ichida migrate (birinchi marta)

```bash
docker exec mahalla_web python manage.py migrate
```

## 6. Tekshirish

```bash
docker compose ps          # konteynerlar holati
docker compose logs web    # Django loglari
docker compose logs nginx  # Nginx loglari
```

Brauzerda: `http://server-ip` — sahifa ochilishi kerak.

---

## Ma'lumotlar qayerda saqlanadi?

- `sqlite_data` Docker volume — db.sqlite3 shu yerda
- `static_files` Docker volume — CSS/JS fayllar
- `media_files` Docker volume — yuklangan rasmlar

Volume'larni zaxiralash:
```bash
docker run --rm -v mahalla_sqlite_data:/data -v $(pwd):/backup alpine \
  tar czf /backup/db_backup.tar.gz /data
```
