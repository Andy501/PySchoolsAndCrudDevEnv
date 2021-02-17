import csv

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponseForbidden, HttpResponse, request
from django.urls import reverse
from .forms import BehaviorForm
from .models import BehaviorGrade
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin
from .models import MemberStudent
from django.views.generic.edit import FormMixin

# Create your views here.


def ExportCSVstudent(request):
    student_lister=MemberStudent.objects.all()
    #students = student_lister.name
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachement; filename="class_roster.csv"'

    writer = csv.writer(response)

    #writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    #for loop on students variable

   #similar logic
    writer.writerow(['Test', student_lister,]) #MemberStudent.age])
    return response



class StudentListView(ListView):
    model = MemberStudent
    template_name = 'student_list.html'

class StudentDetailView(FormMixin,DetailView):
    model = MemberStudent
    template_name = 'student_detail.html'
    form_class = BehaviorForm

    def get_success_url(self):
        return reverse('student_list')#, kwargs={'pk':self.object.pk})


#from stack to populate specific form key
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            behavior_grade = form.save(commit=False)
            behavior_grade.studentName = self.object#passes unammed form field
            behavior_grade.studentName.pk = form.save(commit=True)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        return super().form_valid(form)


#list view of reviews.

#detail view of reviews.

#export class roster to csv