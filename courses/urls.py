from django.urls import path
from .views import CourseListView, CourseDetailView, SearchResultsListView

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]