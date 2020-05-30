from django.urls import path
from django.contrib.auth.decorators import login_required

from courses.views import HomeView,AboutView,ContactView,CourseListView, CourseDetailView, SearchView, create_clas, create_subject, create_teaching

app_name = 'courses'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('courses/<int:category>', CourseListView, name='course_list'),
    path('courses/<slug>/', login_required(CourseDetailView.as_view()), name='course_detail'),
    path('search/', SearchView, name='create_kurs'),
    path('create/class', create_clas, name='create_kurs'),
    path('create/subject', create_subject, name='create_kurs'),
    path('create/teaching', create_teaching, name='create_kurs')
]
