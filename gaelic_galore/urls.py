from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


urlpatterns = [
    # admin for Django
    path('admin/', admin.site.urls),

    # allauth
    path('accounts/', include('allauth.urls')),

    # favicon
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico'))),


    # my local apps
    path('', include('pages.urls')),
    path('courses/', include('courses.urls')),
    path('locations/', include('locations.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
