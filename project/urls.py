from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from dailyInbox.core.views import index

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("anymail/", include("anymail.urls")),
    path("", index, name="index"),
    path("admin/", admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
