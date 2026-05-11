from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pages.urls import api_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/murojaatlar/', include('murojaatlar.urls')),
    path('api/takliflar/', include('takliflar.urls')),
    path('api/', include('elonlar.urls')),
    path('api/', include((api_urlpatterns, 'pages_api'))),
    path('', include('pages.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
