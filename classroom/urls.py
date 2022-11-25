from django.urls import path
from .views import TeacherTemplateView, ContactFormView, TeacherCreateView, TeacherListView, TeacherDetailView, TeacherUpdateView, TeacherDeleteView
from .models import Teacher
from . import views



app_name = 'classroom'


urlpatterns = [
    path('', TeacherTemplateView.as_view(), name = 'home'),
    path('contact_form/',ContactFormView.as_view(), name =  'contact_form'),
    path('create/', TeacherCreateView.as_view(), name= 'create'),
    path('teacher_list', TeacherListView.as_view(), name = 'teacher_list'),
    path('detail_view/<int:pk>', TeacherDetailView.as_view(), name= 'detail_view'),
    path('teacher_update/<int:pk>', TeacherUpdateView.as_view(), name = 'teacher_update'),
    path('teacher_delete/<int:pk>', TeacherDeleteView.as_view(), name = 'teacher_delete')
]