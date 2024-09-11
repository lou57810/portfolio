from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlspatterns += staticfiles_urlpatters()


"""def trigger_error(request):
    division_by_zero = 1 / 0"""


urlpatterns = [
    # path('sentry-debug/', trigger_error),
    path('admin/', admin.site.urls),
    path("", include("blogapi.urls")),  # "" = url 127.0.0.1:8000 et renvoie sur blogapi
    path("", include("authentication.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
    # urlpatterns += static(
    # settings.STATIC_URL, document_root=settings.STATIC_ROOT)
"""Valable uniquement en developpement, avec DEBUG=True,
    MEDIA_URL est l'URL depuis laquelle Django va essayer de servir des medias.
    MEDIA_ROOT indique le répertoire local dans lequel seront sauvegardées les
    images téléversées."""
