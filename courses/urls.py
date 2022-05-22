from django.urls import path
from . import views
from .views import CourseListView, CourseDetailView, SearchResultsListView, AdvancedListView, IntermediateListView, BeginnerListView


urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('advanced/', AdvancedListView.as_view(), name='advanced'),
    path('intermediate/', IntermediateListView.as_view(), name='intermediate'),
    path('beginner/', BeginnerListView.as_view(), name='beginner'),
    path('add/', views.add_course, name='add_course'),
    path('edit/<int:course_id>/', views.edit_course, name='edit_course'),
    path('delete/<int:course_id>/', views.delete_course, name='delete_course'),
    
]