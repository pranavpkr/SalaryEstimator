import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

totalgrosserngsMBA = [42000,44554,57426,59723,62112,91086,94729,98519,102459,131070]
totalgrosserngsCS  = [33000,35006,57426,59723]

def CalculateCAGR(Maturityyears,option):
    if option=="MBA":
        cagr = pow(totalgrosserngsMBA[Maturityyears-1] / totalgrosserngsMBA[0], 1/9) -1
    if option=="CS":
        cagr = pow(totalgrosserngsCS [Maturityyears-1] / totalgrosserngsCS [0], 1/9) -1        
    return cagr

def CalculateSum( StartingSalary, Maturity, CAGR):
    Sum = StartingSalary
    for y in range(Maturity-1):
        CurrentSalary = StartingSalary*(1 + CAGR)
#        print( y,int(StartingSalary), int(CurrentSalary) )
        StartingSalary = CurrentSalary
        Sum+=CurrentSalary
    return Sum

def CalculateRePortn(s,i,cm, m, option):
    return cm*i/CalculateSum(s,m,CalculateCAGR(m, option))
    
def getData(Investment, Maturity, CashMultiple, InitiailInvstmt,
            StartingSalary, InputSalary, Option):
    if Option=="MBA":
        SalaryGrowthRate = 0.1
    else:
        SalaryGrowthRate = 0.03
    
    
    Sum = CalculateSum( StartingSalary, Maturity, CalculateCAGR(Maturity, Option) )

    EdbgRate= CalculateRePortn( StartingSalary, Investment, CashMultiple, Maturity, Option)
#    print("EdbgRate:", EdbgRate*100 )
    
    BankRate = pow( EdbgRate*Sum/InitiailInvstmt, 1/Maturity)-1
#    print("BankRate:",BankRate*100 )
    
    
    #For Graph
    try:
        k = (pow(1+BankRate, Maturity)-1)/( BankRate*(pow(1+BankRate, Maturity)))
        
        Er = []; Br = [];Yr =[]
        for i in range(Maturity):
            if i==0:rate = EdbgRate*InputSalary
            nextrate = rate*(1+SalaryGrowthRate)
        #    print(i+2000, Investment/k, rate)
            Yr.append(2000+i); Er.append(rate); Br.append(Investment/k)
            rate = nextrate
     
        Legend=['BankRate','EdbrgRate']
        pos = np.arange(len(Yr))
        bar_width = 0.35
         
        plt.bar(pos,Br,bar_width,color='grey',edgecolor='black')
        plt.bar(pos+bar_width,Er,bar_width,color='blue',edgecolor='black')
        plt.xticks(pos, Yr)
        plt.title('Payments for Edbrg vs Bank',fontsize=18)
        plt.legend(Legend,bbox_to_anchor=(0.5, -0.18),frameon=False, loc='lower center', ncol=2)
    except:pass
#    plt.show()
    
    return EdbgRate, BankRate, plt

if __name__ == "__main__":#Inputs
    StartingSalary = 20000
    Investment     = 30000
    InitiailInvstmt= 30000
    
    InputSalary    = 41000
    CashMultiple   = 2
    Maturity       = 3
    Option         = "MBA"
    
    getData( Investment, Maturity, CashMultiple, InitiailInvstmt,
            StartingSalary, InputSalary, Option)


