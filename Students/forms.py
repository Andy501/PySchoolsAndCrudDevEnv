from django import forms
from django.forms import ModelForm
from django.views.generic import DetailView
from Students.models import BehaviorGrade

#is th3e detial view new or existing?


#reread form docs to pass correct vars befor testing.
class BehaviorForm(ModelForm):
    class Meta:
        model = BehaviorGrade
        fields = ['eventGrade',
                  'eventSeverity','eventTitle',
                  'eventDescription']

