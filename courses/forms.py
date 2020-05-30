from django import forms
from .models import Clas, Subjects, Lesson



class ClasForm(forms.ModelForm):
    class Meta:
        model = Clas
        fields = '__all__'
        help_texts = {
            'title': ' ex:Fundamental Algorithms',
            'decrition':' Desccribe course shortly',
            'image':'You can place a class photo or it can be left blank'
        }

class SubjectsForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ['createdby','slug', 'title', 'clas', 'description', 'img']
        help_texts = {
            'title': 'ex. Fisrt part, Second part',
            'description':'Desccribe subject lab shortly',
        }
        widgets = {'creator': forms.HiddenInput(), 'slug': forms.HiddenInput()}


class TeachingForm(forms.ModelForm):
    class Meta:
        model = Lesson 
        fields = ['slug','title', 'subjects', 'video_id', 'position', ]
        widgets = {
            'slug': forms.HiddenInput()
        }