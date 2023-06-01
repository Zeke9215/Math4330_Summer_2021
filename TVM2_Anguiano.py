from tkinter import *
from tkinter import messagebox
from math import *

root =Tk()
root.title('Time Value of Money Calculator')
root.geometry('700x370')
root.resizable(width=False, height=False)



def ppy_labels(value):
    ppy.config(label=str(scale[int(value)]))
    cpy.set(value)
def cpy_labels(value):
    cpy.config(label=str(scale[int(value)]))



def tvm():
    s=eb.get()
    j=scale[int(ppy.get())]
    k=scale[int(cpy.get())]
    n=eval(nb.get()) if nb.get()!='' else nb.get()
    r=eval(rt.get()) if rt.get()!='' else rt.get()
    P=eval(pv.get()) if pv.get()!='' else pv.get()
    Q=eval(pm.get()) if pm.get()!='' else pm.get()
    F=eval(fv.get()) if fv.get()!='' else fv.get()
    error1='Cash flows in different directions need to have opposite signs!'
    error2='Check your data!'
    error3='Which one do you want to solve?'
    if [n,r,P,Q,F].count('')!=1:
        messagebox.showerror('error',error3)
    else:
        t=[n,r,P,Q,F].index('')
    if t<2 and max([P,Q,F])*min([P,Q,F])>0:
        messagebox.showerror('error',error1)
    elif t!=1:
        u=(1+r/(100*k))**(k/j)
    else:
        pass
    if t==0:
        v=(Q*(1-s+s*u)-F*(u-1))/(P*(u-1)+Q*(1-s+s*u))
        if v<=0:
            messagebox.showerror('errorâ€™,error2')
        else:
            y=log(v)/log(u)
            nb.set(str(y))
    elif t==1:
        f=lambda x:(x*(((Q*s+P)*(n-1)*x*x+((n-s-2)*Q-P)*x-2*Q)*(1+x)**n+
                        (1+x)*((Q*s-F)*x+2*Q))/((n*(Q*s+P)*x*x+Q*(n-1)*x-Q)*(1+x)**n+Q*(1+x)))
        z=-(n*Q+F+P)/(n*(Q*s+P))
        for i in range(15):z=f(z)
        y=100*k*((1+z)**(j/k)-1)
        rt.set(str(y))
    elif t==2:
        y=-(Q*(u**n-1)*(1-s+s*u)/(u-1)+F)/u**n
        pv.set(str(y))
    elif t==3:
        y=-(F+P*u**n)*(u-1)/((u**n-1)*(1-s+s*u))
        pm.set(str(y))
    else:
        y=-P*u**n-Q*(u**n-1)*(1-s+s*u)/(u-1)
        fv.set(str(y))



def clear():
    nb.set('')
    rt.set('')
    pv.set('')
    pm.set('')
    fv.set('')
    ppy.set(0)
    cpy.set(0)
    eb.set(0)





def popup():
    txt="""The TVM calculator can be used to calculate various
quantities related to the time value of money such as present value,
future value, interest rate, and repeated payments for a loan or a
saving account. To use it, leave the quantity to be calculated blank,
fill in the other quantities, choose the numbers of payments and
compounding per year and whether they are end-of-period payments or
beginning-of-period payments, and click the "Calculate" button.
Note that the cash flows in different directions need to have opposite
signs. For example, the initial loan amount (from bank to borrower)
and the monthly payment (from borrower to bank) need to have opposite
signs, if one is positive, the other must be negative."""

    h = Toplevel()
    h.geometry('600x300')
    h.title('Help')
    h.resizable(width=False, height=False)
    l=Label(h,text='How to use the TVM calculator')
    l.config(font=('Courier', 14))
    l.pack()
    t= Text(h, height = 12, width = 70)
    t.pack(pady=15)
    t.insert('1.0', txt)
    button=Button(h, text='Close', command=h.destroy)
    button.pack()

   




menubar = Menu(root)
menubar.add_command(label='Help',command=popup)
root.config(menu=menubar)

frame1=Frame(root)
frame1.grid(row=0,column=0,pady=20)

frame2=Frame(root)
frame2.grid(row=1,column=0,pady=10)

frame3=Frame(root)
frame3.grid(row=2,column=0,pady=5)

frame4=Frame(root)
frame4.grid(row=3,column=0,pady=5)

frame5=Frame(root)
frame5.grid(row=5,column=0,pady=5)

frame6=Frame(root)
frame6.grid(row=6,column=0,pady=30)






nb=StringVar()
rt=StringVar()
pv=StringVar()
pm=StringVar()
fv=StringVar()
eb=IntVar()
eb.set(0)
scale = {0:1,1:2,2:3,3:4,4:6,5:12,6:365}




Label(frame1, text='Number of Payments:'
      ).grid(row=0,column=0,padx=(50,10))
Entry(frame1, width=15, textvariable=nb).grid(row=0,column=1,padx=(10,45))
Label(frame1,text='Interest Rate per Year:'
      ).grid(row=0,column=2,padx=(40,10))
Entry(frame1, width=15, justify=RIGHT, textvariable=rt).grid(row=0,column=3,padx=(10,5))
Label(frame1, text='%').grid(row=0,column=4,padx=(5,5))



Label(frame2,text = 'Present Value:').grid(row=0,column=0,padx=(30,10))
Label(frame2,text ='$').grid(row=0,column=1,padx=(3,3))
Entry(frame2, width=15, textvariable=pv).grid(row=0,column=2,padx=(2,15))
Label(frame2,text ='Payment:').grid(row=0,column=3,padx=(15,5))
Label(frame2,text ='$').grid(row=0,column=4,padx=(3,3))
Entry(frame2, width=15, textvariable=pm).grid(row=0,column=5,padx=(2,15))
Label(frame2,text ='Future Value:').grid(row=0,column=6,padx=(15,5))
Label(frame2,text ='$').grid(row=0,column=7,padx=(3,3))
Entry(frame2, width=15,textvariable=fv).grid(row=0,column=8,padx=(2,0))



Label(frame3, text ='Number of Payment per Year:'
).grid(row=0,column=0,pady=(10,0),padx = (32,58))
ppy=Scale(frame3, from_=0, to=6, tickinterval= 0, label='1',
orient=HORIZONTAL,length=200, showvalue=0,resolution=1,command=ppy_labels)
ppy.grid(row=0, column=1)
frame3a=Frame(frame3)
frame3a.grid(row=1,column=1)



Label(frame3a,text='1').grid(row=0, column=0,padx = (8, 8))
Label(frame3a,text='2').grid(row=0, column=1,padx = (8, 8))
Label(frame3a,text='3').grid(row=0, column=2,padx = (8, 8))
Label(frame3a,text='4').grid(row=0, column=3,padx = (8, 8))
Label(frame3a,text='6').grid(row=0, column=4,padx = (8, 8))
Label(frame3a,text='12').grid(row=0, column=5,padx = (5, 3))
Label(frame3a,text='365').grid(row=0, column=6,padx = (4, 0))



Label(frame4, text ='Number of Compounding per Year:'
        ).grid(row=0,column=0,pady=(10,0),padx = 30)
cpy=Scale(frame4, from_=0, to=6, tickinterval= 0, label='1',
                orient=HORIZONTAL,length=200, showvalue=0,resolution=1,command=cpy_labels)
cpy.grid(row=0, column=1)
frame4a=Frame(frame4)
frame4a.grid(row=1,column=1)



Label(frame4a,text='1').grid(row=0, column=0,padx = (8, 8))
Label(frame4a,text='2').grid(row=0, column=1,padx = (8, 8))
Label(frame4a,text='3').grid(row=0, column=2,padx = (8, 8))
Label(frame4a,text='4').grid(row=0, column=3,padx = (8, 8))
Label(frame4a,text='6').grid(row=0, column=4,padx = (8, 8))
Label(frame4a,text='12').grid(row=0, column=5,padx = (5, 3))
Label(frame4a,text='365').grid(row=0, column=6,padx = (4, 0))



Radiobutton(frame5, text='End-of-Period Payments',value=0, variable=eb
).grid(row=0,column=0,padx=(32,40))
Radiobutton(frame5, text='Beginning-of-Period Payments',value=1, variable=eb
).grid(row=0,column=1,padx=(40,0))



Button(frame6, width=10, text = 'Calculate',command=tvm
       ).grid(row=0, column=0,padx = (25, 40))
Button(frame6, width=10, text = 'Clear',command=clear
       ).grid(row=0, column=1,padx = (40, 40))
Button(frame6, width=10, text = 'Close',command=root.destroy
       ).grid(row=0, column=2,padx = (40, 0))

root.mainloop()
