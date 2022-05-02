from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # admin for Django
    path('admin/', admin.site.urls),

    # allauth
    path('accounts/', include('allauth.urls')),

    # my local apps
    path('', include('pages.urls')),
    path('courses/', include('courses.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
