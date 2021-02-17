from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Teachers


# Create your views here.
def index(request):
    return render(request, 'index.html')

class TeacherListView(ListView):
    model = Teachers
    template_name = 'teacher_list.html'


class TeacherDetailView(DetailView):
    model = Teachers
    template_name = 'teacher_detail.html'
