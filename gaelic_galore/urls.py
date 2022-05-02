from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # admin for Django
    path('admin/', admin.site.urls),

    # allauth
    path('accounts/', include('allauth.urls')),

    # my local apps
    path('', include('pages.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
