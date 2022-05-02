from django.urls import path
from .views import LocationListView, CourseListView

urlpatterns = [
    path('', LocationListView.as_view(), name='location_list'),
    path('', CourseListView.as_view(), name='course_list'),
]