from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Course
from django.db.models import Q
from .forms import CourseForm

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
# returns filtered results from the navbar search
    model = Course
    context_object_name = 'course_list'
    template_name = 'courses/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Course.objects.filter(
            Q(location__name__icontains=query) |
            Q(location__description_place__icontains=query) |
            Q(location__description_accomodation__icontains=query) |
            Q(location__closing_remarks__icontains=query) |
            Q(title__icontains=query)    |
            Q(level__icontains=query)   |
            Q(course_description__icontains=query)
        )
    """ Note from the above the different syntax required when
    searching on a foreign key!!!!"""



class AdvancedListView(ListView):
# returns a filtered view with advanced courses
    model = Course
    template_name = 'courses/advanced.html'

    def get_queryset(self):
        return Course.objects.all().filter(level='Advanced')

class IntermediateListView(ListView):
# returns a filtered view with intermediate courses
    model = Course
    template_name = 'courses/intermediate.html'

    def get_queryset(self):
        return Course.objects.all().filter(level='Intermediate')

class BeginnerListView(ListView):
# returns a filtered view with beginner courses
    model = Course
    template_name = 'courses/beginner.html'

    def get_queryset(self):
        return Course.objects.all().filter(level='Beginner')

@login_required
def add_course(request):
# adds course to the site
    if not request.user.is_superuser:
        messages.error(request, 'Tha sinn duilich. This page is only for site admin.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'Sgonneil! New course added!')
            return redirect(reverse('course_detail', args=[course.id]))
        else:
            messages.error(request, 'Tha sinn duilich! Failed to add course.')
    else:
        form = CourseForm()
        
    template = 'courses/add_course.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_course(request, course_id):
# edits a course on the site
    if not request.user.is_superuser:
        messages.error(request, 'Tha sinn duilich. This page is only for site admin.')
        return redirect(reverse('home'))
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sgonneil! Updated course!')
            return redirect(reverse('course_detail', args=[course.id]))
        else:
            messages.error(request, 'Tha sin duilich. Failed to update course.')
    else:
        form = CourseForm(instance=course)
        messages.info(request, f'You are editing {course.title}')

    template = 'courses/edit_course.html'
    context = {
        'form': form,
        'course': course,
    }

    return render(request, template, context)


@login_required
def delete_course(request, course_id):
    # delete course store site
    if not request.user.is_superuser:
        messages.error(request, 'Tha sinn duilich. This page is only for site admin.')
        return redirect(reverse('home'))
    course = get_object_or_404(Course, pk=course_id)
    course.delete()
    messages.success(request, 'Sgonneil! Course deleted!')
    return redirect(reverse('course_list'))