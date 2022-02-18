from dataclasses import field
from datetime import datetime
from django import forms
from django.forms import DateTimeInput, ModelForm
from django.contrib.admin.widgets import AdminSplitDateTime,AdminDateWidget
from .models import *
from django import forms

# class DateForm(forms.Form):
#     date = forms.DateTimeField(
#         input_formats=['%d/%m/%Y %H:%M'],
#         widget=forms.DateTimeInput(attrs={
#             'class': 'form-control datetimepicker-input',
#             'data-target': '#datetimepicker1'
#         })
#     )
class DateInput(forms.DateInput):
    input_type='date'
class TaskForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Task Title..'}),label=False)
    # due=forms.DateTimeField(widget = forms.DateTimeInput( format='%d/%m/%Y %H:%M'))
   
    # due = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    due = forms.DateTimeField(widget=DateInput)
    class Meta:
        model=task
        
        fields=['title','due']
class UpdateForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Task Title..'}),label=False)
    due = forms.DateTimeField(widget=DateInput)
    class Meta:
        model=task
        fields=['title','due','complete']
class UserForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user']
