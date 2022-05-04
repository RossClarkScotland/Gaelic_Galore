from django.views.generic import ListView, DetailView
from .models import Course

# Create your views here.
class CourseListView(ListView):
# returns all courses
    model = Course
    context_object_name = 'course_list'
    template_name = 'courses/course_list.html'

class CourseDetailView(DetailView):
# returns individual courses
    model = Course
    context_object_name = 'course'
    template_name = 'courses/course_detail.html'

