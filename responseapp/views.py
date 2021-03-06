from django.shortcuts import render
from responseapp.forms import MyForm
from django.template import loader
from django.http import HttpResponse
from responseapp.est import plotSalary

from pylab import *
import matplotlib
matplotlib.use('Agg')
#import matplotlib.pyplot as plt
from matplotlib import pylab
from io import BytesIO
import urllib, base64

def responseform(request):
#if form is submitted
    request.POST = request.POST.copy()
    if request.method == 'POST':
        myForm = MyForm(request.POST)

        if myForm.is_valid():
            StartingSalary = myForm.cleaned_data['StartingSalary']
            YearlyHikePercent = myForm.cleaned_data['YearlyHikePercent']
            PromotionCycle = myForm.cleaned_data['PromotionCycle']
            Tenure = myForm.cleaned_data['Tenure']
            
            Slist,plt = plotSalary(StartingSalary, YearlyHikePercent,
                                   PromotionCycle, Tenure)

            fig = plt.gcf()
            fig.set_size_inches(8,4.4, forward=True)
            buf = BytesIO()

            fig.savefig(buf, format='png')
            fig.clf()

            buf.seek(0)
            string = base64.b64encode(buf.read())

            uri = 'data:image/png;base64,' + urllib.parse.quote(string)
            args = {'form':myForm, 'image':uri}
            buf.truncate(0)
            
#            return HttpResponse(buffer.getvalue(), content_type="image/png")
            return render(request, 'responseform.html', args)
#            return render(request, 'responseform.html', {'form':myForm} )

    else:
         form = MyForm()

    return render(request, 'responseform.html', {'form':form})