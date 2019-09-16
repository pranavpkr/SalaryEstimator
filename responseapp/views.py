from django.shortcuts import render
from responseapp.forms import MyForm
from django.template import loader
from django.http import HttpResponse
from responseapp.edbridg import getData

#import matplotlib.pyplot as plt
#from matplotlib import pylab
#from pylab import *
#import PIL, PIL.Image
#from io import BytesIO
#import urllib, base64

def responseform(request):
#if form is submitted
    request.POST = request.POST.copy()
    if request.method == 'POST':
        myForm = MyForm(request.POST)

        if myForm.is_valid():
            Investment = myForm.cleaned_data['Investment']
            StartingSalary = myForm.cleaned_data['StartingSalary']
            InitiailInvstmt = myForm.cleaned_data['InitiailInvstmt']
            InputSalary = myForm.cleaned_data['InputSalary']
            CashMultiple = myForm.cleaned_data['CashMultiple']
            Maturity = myForm.cleaned_data['Maturity']
            Option = myForm.cleaned_data['Option']
            
#            if myForm.cleaned_data["Option"] == "CS":
#                myForm.fields["Maturity"].max_value = 4

            EdbgRate, BankRate = getData(Investment, Maturity, CashMultiple, InitiailInvstmt,
                        StartingSalary, InputSalary, Option)

            request.POST.__setitem__("ER", EdbgRate*100)
            request.POST.__setitem__("BR", BankRate*100)
            
            '''
            fig = plt.gcf()
            buf = BytesIO()

            fig.savefig(buf, format='png')
            fig.clf()

            buf.seek(0)
            string = base64.b64encode(buf.read())

            uri = 'data:image/png;base64,' + urllib.parse.quote(string)
            args = {'form':myForm, 'image':uri}
            buf.truncate(0)
            '''
#            return HttpResponse(buffer.getvalue(), content_type="image/png")
#            return render(request, 'responseform.html', args)
            return render(request, 'responseform.html', {'form':myForm} )

    else:
         form = MyForm()

    return render(request, 'responseform.html', {'form':form})