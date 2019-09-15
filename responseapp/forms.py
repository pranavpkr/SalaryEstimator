from django import forms
from django.core.validators import MaxValueValidator
from django.db import models

School_CHOICES= [
    ('CS',  'Coding School'),
    ('MBA', 'MBA School'),
    ]

class MyForm(forms.Form):
    Investment = forms.IntegerField(initial = 10000, min_value=5000, max_value=50000)
    InitiailInvstmt = forms.IntegerField(initial = 10000)
    StartingSalary = forms.IntegerField(initial = 20000)
    InputSalary = forms.IntegerField(initial = 20000)
    CashMultiple = forms.FloatField(initial = 2, min_value=0.1, max_value=2.0)
    Maturity = forms.IntegerField(initial = 4,min_value=2, max_value=10)    
    Option = forms.CharField( widget=forms.Select(choices=School_CHOICES))
    ER = forms.FloatField( required=False)
    BR = forms.FloatField( required=False)

    def setER(self, value):
        super(MyForm, self)
        self.fields['ER'].value = value