import secrets
from django.shortcuts import render, redirect
from django.views.generic import TemplateView,ListView,DetailView,View
from courses.models import Subjects,Lesson,Clas
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ClasForm, SubjectsForm, TeachingForm
# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Clas.objects.all()
        context['category'] = category
        return context

class AboutView(TemplateView):
    template_name = 'about.html'


def CourseListView(request, category):
    courses = Subjects.objects.filter(category)
    context = {
        'courses':courses
    }
    return render(request, 'courses/course_list.html', context)



class CourseDetailView(DetailView):
    context_object_name = 'course'
    template_name = 'courses/course_detail.html'
    model = Subjects



@login_required
def SearchView(request):
    if request.method == 'POST':
        s = request.POST.get('search')
        results = Lesson.objects.filter(s)
        context = {
            'results':results
        }
        return render(request, 'courses/search_result.html', context)


@login_required
def create_clas(request):
    if not request.user.profile.is_teacher == True:
        messages.error(request, f'Your account does not have access to this url only teacher accounts!')
        return redirect('courses:home')
    if request.method == 'POST':
        form = ClasForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your class was created.')
            return redirect('courses:home')
    else:
        form = ClasForm()
    context = {
        'form':form
    }
    return render(request, 'courses/create_class.html', context)


@login_required
def create_subject(request):
    if not request.user.profile.is_teacher == True:
        messages.error(request, f'Your account does not have access to this url only teacher accounts!')
        return redirect('courses:home')
    if request.method == 'POST':
        form = SubjectsForm(request.POST)
        if form.is_valid():
            form.save()
            clas = form.cleaned_data['klasa']
            slug = clas.id
            messages.success(request, f'Your subject was created.')
            return redirect('/courses/' + str(slug))
    else:
        form = SubjectsForm(initial={'creator':request.user.id, 'slug':secrets.token_hex(nbytes=16)})
    context = {
        'form':form
    }
    return render(request, 'courses/create_subject.html', context)


@login_required
def create_teaching(request):
    if not request.user.profile.is_teacher == True:
        messages.error(request, f'Your account does not have access to this url only teacher accounts!')
        return redirect('courses:home')
    if request.method == 'POST':
        form = TeachingForm(request.POST)
        if form.is_valid():
            form.save()
            legend = form.cleaned_data['lenda']
            slug = legend.slug
            messages.success(request, f'Your lesson was created.')
            return redirect('/courses/' + str(slug) )
    else:
        form = TeachingForm(initial={'slug':secrets.token_hex(nbytes=16)})
    context = {
        'form':form
    }
    return render(request, 'courses/create_teaching.html', context)


def view_404(request, exception):
    return render(request, '404.html')

def view_403(request, exception):
    return render(request, '403.html')

def view_500(request):
    return render(request, '500.html')
