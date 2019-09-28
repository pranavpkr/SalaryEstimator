from django import forms
from django.core.validators import MaxValueValidator
from django.db import models

#School_CHOICES= [
#    ('CS',  'Coding School'),
#    ('MBA', 'MBA School'),
#    ]

class MyForm(forms.Form):
    StartingSalary = forms.IntegerField(initial = 10000)
    YearlyHikePercent = forms.FloatField(initial = 10, min_value=0.0, max_value=100.0)
    PromotionCycle = forms.IntegerField(initial = 2,min_value=1, max_value=5)    
    Tenure = forms.IntegerField(initial = 3)
#    Option = forms.CharField( widget=forms.Select(choices=School_CHOICES))