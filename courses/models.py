from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Clas(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length= 200, null=True)
    image = models.ImageField(upload_to='cat_images', default='cat_images/default.jpg')

    def __str__(self):
        return '{}'.format(self.title)

class Subjects(models.Model):
    creator = models.ForeignKey(User,on_delete = models.CASCADE)
    slug = models.SlugField()
    title = models.CharField(max_length=30)
    cl = models.ForeignKey(Clas,on_delete=models.CASCADE)
    description = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now=True)
    curs_img = models.ImageField(upload_to='kurs_images', default='default.jpg')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:course_detail", kwargs={"slug": self.slug})

    @property
    def lessons(self):
        return self.lesson_set.all().order_by('position')




class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=30)
    legend = models.ForeignKey(Subjects,on_delete=models.CASCADE)
    video_id = models.CharField(max_length=11)
    position= models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:lesson_detail", kwargs={"course_slug": self.legend.slug,'lesson_slug':self.slug})
