from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # admin for Django
    path('admin/', admin.site.urls),

    # allauth
    path('accounts/', include('allauth.urls')),

    # my local apps
    path('', include('pages.urls')),
]
