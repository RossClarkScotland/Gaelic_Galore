from django.urls import path
from . import views
from .views import LocationListView, LocationDetailView

urlpatterns = [
    path('', LocationListView.as_view(), name='location_list'),
    path('<int:pk>/', LocationDetailView.as_view(), name='location_detail'),
    path('add/', views.add_location, name='add_location'),
    path('edit/<int:location_id>/', views.edit_location, name='edit_location'),
    path('delete/<int:location_id>/', views.delete_location, name='delete_location'),
    path('delete/<int:location_id>/', views.delete_location, name='delete_location'),
]
