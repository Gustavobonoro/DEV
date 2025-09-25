from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView # Importe o RedirectView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', RedirectView.as_view(url='/catalogo/', permanent=True)),
    path('admin/', admin.site.urls),
    path('catalogo/', include('catalogo.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
