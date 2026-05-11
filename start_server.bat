@echo off
echo Mahalla Smart Platform serveri ishga tushmoqda...
echo.
echo  Sayt:           http://127.0.0.1:8000/
echo  Kirish:         http://127.0.0.1:8000/login/
echo  Xizmatlar:      http://127.0.0.1:8000/xizmatlar/
echo  Admin panel:    http://127.0.0.1:8000/admin-panel/
echo  Django admin:   http://127.0.0.1:8000/django-admin/
echo.
echo  Admin kirish:   admin@mahalla.uz / admin1234
echo.
cd /d %~dp0
python manage.py runserver
