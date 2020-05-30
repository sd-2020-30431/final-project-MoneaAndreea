from django.contrib import admin
from courses.models import Lesson,Subjects,Clas
# Register your models here.

admin.site.register(Subjects)
admin.site.register(Lesson)
admin.site.register(Clas)
