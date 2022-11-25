from msilib.schema import ListView
from typing import List
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView

from .forms import ContactFrom
from .models import Teacher

# Create your views here.


class TeacherTemplateView(TemplateView):
    template_name = 'classroom/home.html'


class ContactFormView(FormView):
    form_class = ContactFrom
    template_name = 'classroom/contact.html'

    success_url = reverse_lazy('classroom:home')

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)


class TeacherCreateView(CreateView):
    model = Teacher 
    fields = '__all__'

    success_url = reverse_lazy('classroom:home')

class TeacherListView(ListView):
    model = Teacher

class TeacherDetailView(DetailView):
    model = Teacher 


class TeacherUpdateView(UpdateView):
    model = Teacher 
    fields = '__all__'
    success_url = reverse_lazy('classroom:teacher_list')


class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('classroom:teacher_list')