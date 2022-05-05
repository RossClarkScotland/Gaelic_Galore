from django.views.generic import ListView, DetailView
from .models import Course
from django.db.models import Q

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

class SearchResultsListView(ListView):
    model = Course
    context_object_name = 'course_list'
    template_name = 'courses/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Course.objects.filter(
            Q(location__name__icontains=query) |
            Q(location__description_place__icontains=query) |
            Q(location__description_accomodation__icontains=query) |
            Q(title__icontains=query)    |
            Q(level__icontains=query)
        )
    """ Note from the above the different syntax required when
    searching on a foreign key!!!!"""



class AdvancedListView(ListView):
    model = Course
    template_name = 'courses/advanced.html'

    def get_queryset(self):
        return Course.objects.all().filter(level='Advanced')

class IntermediateListView(ListView):
    model = Course
    template_name = 'courses/intermediate.html'

    def get_queryset(self):
        return Course.objects.all().filter(level='Intermediate')

class BeginnerListView(ListView):
    model = Course
    template_name = 'courses/beginner.html'

    def get_queryset(self):
        return Course.objects.all().filter(level='Beginner')

