# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def plotSalary( ss, yh, pc, t ):
#    print( ss, yh, pc, t )
    slist = []; Yr=[]
    for i in range(1,t+1):
        if i%pc == 0:
            cs = ss+(0.2*ss)
        else:
            cs = ss+(0.1*ss)
        slist.append(cs)
        Yr.append(i)
#        print( cs, i%pc, i)
        ss=cs
    Legend=['Salary']
    pos = np.arange(len(Yr))
    bar_width = 0.35
     
    plt.bar(pos,slist,bar_width,color='blue',edgecolor='black')

    plt.xticks(pos, Yr)
    plt.title('Salary Estimate',fontsize=15)
    plt.legend(Legend,bbox_to_anchor=(0.5, -0.18),frameon=False, loc='lower center', ncol=2)

    return slist, plt

if __name__ == "__main__":#Inputs
    StartingSalary = 550000
    YearlyHikePercent  = 10
    PromotionCycle = 3
    Tenure = 8

    slist = plotSalary( StartingSalary, YearlyHikePercent, PromotionCycle, Tenure )
    print(slist)