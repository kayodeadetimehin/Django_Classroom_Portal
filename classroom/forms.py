from tkinter import Widget
from django import forms
from django.forms import Textarea



class ContactFrom(forms.Form):
    name = forms.CharField()
    Message = forms.CharField(widget=forms.Textarea)

    