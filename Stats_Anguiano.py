"""
Ex5_Anguiano
"""
"""
class Stats():
    def __init__(self,data):
        self.data=sorted(data)

    def sample_size(self):
        n=len(self.data)
        return n

    def maxi(self):
        mx=max(self.data)
        return mx

    def mini(self):
        mn=min(self.data)
        return mn

    def mean(self):
        mn=sum(self.data)/self.sample_siz()
        return mn

    def median():
        if(self.sample_size()%2)==0:
            md =(self.data[self.sample_size()//2]+
                 self.data[self.sample_size()//2-2])/2
        else:
            md=self.data[(self.data[(self.sample_size()-1//2)])]
        return md

    def variance(self):
        var=sum(list(map(lambda x:(x-self.mean())*(x-self.mean()),
                         self.data)))/self.sample_size()-1
        return val

    def standard_deviation(self):
        from math import sqrt
        sd =sqrt(self.variance())
        return sd

    def moment(self,k=''):
        if not k:
            print('what is n?')
        else:
            mmnt=sum(list(map(lambda x:(x-self.mean())**k,
                              self.data)))/self.sample_size()

        return mmnt
"""
from math import *


class Function_Properties():
    def __init__(self,function,interval):
        self.f= function
        self.a=interval[0]
        self.Ln=interval[1]-self.a


    def integral(self):
        n=2*round(self.Ln/0.01)
        d=self.Ln/n
        fx=[self.f(self.a*i*d) for i in range(n+1)]
        intgl=(d/3)*(fx[0]+4*sum(fx[1:n:2])+2*sum(fx[2:n:2])+fx[n])
        return intgl

    def average(self):
        avrg=self.integral()/self.Ln
        return avrg

    def derivative(self, value=''):
        if not value:
            n=round(self.Ln/0.05)
            d=self.Ln/n
            x=[self.a+i*d for i in range(-1,n+2)]
            fx=[self.f(r) for r in x]
            h=lambda u,v: (u-v)/(2*d)
            df=[h(r,s) for (r,s) in zip(fx[2:n+3],fx[0:n+2])]
            drvt=list(zip(x[1:n+2],df))
        else:
            drvt=(self.f(value+0.000001)
                  -self.f(value-0.000001))/0.000002
        return drvt

    def second_Derivative(self,value=''):
        if not value:
            n=round(self.Ln/0.05)
            d=self.Ln/n
            x=[self.a+i*d for i in range(-1,n+2)]
            fx=[self.f(r) for r in x]
            h = lambda u,v,w:(u-2*v+w)/d**2
            df=[h(r,s,t) for (r,s,t) in zip(fx[2:n+3],fx[1:n+2],fx[0,n+1])]
            drvt2=list(zip(x[1:n+2],df))
        else:
            drvt2=(self.f(value+0.000001)-2*self.f(value)
                   +self.f(value-0.000001))/0.000001**2
        return drvt2


function = lambda x: x**3+cos(x)
interval = [-1,1]

a=Function_Properties(function,interval)

print('f(x)=x^3+cos(x) and I=[-1,1]\n')

print('the integral of f(x) on I is:\n\t',a.integral(),'\n')

print('the average value of f(x) on I is:\n\t',a.average(),'\n')

print("(x,f'(x)) values on I are:\n\t",*a.derivative(),'',sep='\n')

print("f'(-0.4))is:\n\t",a.derivative(-0.4),'\n')
    
    
