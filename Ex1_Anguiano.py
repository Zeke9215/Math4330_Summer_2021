"""
Exercise 1
7/6/2022


#SquareRoot Function
def SqRoot(point,tolerance):
    x=point
    y=(x+point/x)/2
    while abs(y-x)>= tolerance:
        x=y
        y=(x+point/x)/2
    return y
print(SqRoot(5,10**(-6)))


#Bi-section Method Function
def biSection(function,bound,tolerance):
    #Finding a zero of a function by the bi-section Method
    a=bound[0]
    b=bound[1]
    f=function
    t=tolerance
    if f(a)*f(b)>0:raise Exception('Error: f(a)f(b)>0')
    while abs(a-b)>=t:
        y = (a+b)/2
        if f(y)*f(b)<0: a=b
        b=y
    return y


print(biSection.__doc__)
import math
print(math.pi.__doc__)
print(math.cos.__doc__)


#bisection example to find zeros
from math import *
fa=lambda x: x-cos(x)
fb=lambda x: 3*x-exp(x)
print('a zero of x-cos(x) in [0,1] is: \n\t',
    biSection(fa,[0,1],0.000001), '\n\n')
print('a zero of 3x-exp(x) in [0,1] is \n\t',
      biSection(fb,[0,1],0.000001),'\n\n')

"""


from math import *
#The Newton Method
def Newton(function,derivative,initial,tolerance):
    """This computes the zeros of a function using Newtons Method"""
    f = function
    df = derivative
    t = tolerance
    p = initial
    g=lambda x: x - (f(x)/df(x))
    q=g(p)
    while abs(p-q)>=t:
        p=q
        q=g(p)
    return q 
    

#Problem A.
f = lambda x: x-cos(x)
df = lambda x: 1+sin(x)
print('The zero for f(x) = x-cos(x) on interval [0,1] is\n\t',Newton(f,df,1,10**(-6)))

#Problem B.
f2 = lambda x: 2+sin(x)-x
df2 = lambda x: cos(x)-1
print('the zero for f(x)=2+sin(x)-x on interval [2,3] is \n\t',Newton(f2,df2,2,10**-6)) 



#FalsePosition function
#Problem C.
def FalsePosition(function,bound,tolerance):
    """This computes the zeros of a function using the False Position Method"""
    f = function
    a=bound[0]
    b=bound[1]
    if f(a)*f(b) > 0: raise Exception('Error: f(a)f(b)>0!')
    g = lambda v,u: v-f(v)*(v-u)/(f(v)-f(u))
    y=a
    while abs(y-b)>=tolerance:
        y = b
        b = g(a,b)
        if f(y)*f(b)<0: a=y 
    return b
    
f = lambda x: 3*x**2 - exp(x)
bound = [-1,0]
print('zeros for f(x)=3x^2 -e^x on interval [-1,0] is \n\t',FalsePosition(f,bound,10**-6))


#Problem D.
boundD = [0,2]
print('zeros for f(x)=3x^2 -e^x on interval [0,2] is \n\t',FalsePosition(f,boundD,10**-6))


#Problem E.
boundE = [2,4]
print('zeros for f(x)=3x^2 -e^x on interval [2,4] is \n\t',FalsePosition(f,boundE,10**-6))
