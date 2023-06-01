
from tkinter import *

root=Tk()
root.title('Mortage Payment Calculator')
root.geometry('350x200')
root.resizable(width=False, height=False)

def calculate():
 p=float(amount.get())
 n=int(year.get())
 r=float(rate.get())
 v=1200/(1200+r)
 m=12*n
 pm=p*(1-v)/(v*(1-v**m))
 pm=str(round(pm,2))
 payment.configure(text = pm)

def clear():
 amount.delete(first=0,last=END)
 year.delete(first=0,last=END)
 rate.delete(first=0,last=END)
 payment.configure(text = '')

Label(root,text = 'Loan Amount:'). place(x=40,y=25)
Label(root,text = '$').place(x=180,y=25)
amount = Entry(root, width=15)
amount.place(x=210,y=25)

Label(root,text = 'Number of years of the Loan:').place(x=40,y=55)
year=Entry(root, width=7)
year.place(x=260,y=55)

Label(root,text = 'Annual Percentage of the Loan:').place(x=40,y=85)
rate=Entry(root, width=12, justify=RIGHT)
rate.place(x=210, y=85)
Label(root,text = '%').place(x=290,y=85)

Label(root,text='Monthly Payment:').place(x=40,y=115)
Label(root,text='$').place(x=180,y=115)
payment=Label(root,text='')
payment.place(x=210,y=115)

Button(root, width=10, text= 'Calculate',command=calculate).place(x=40,y=150)
Button(root, width=10, text= 'Clear',command=clear).place(x=135,y=150)
Button(root, width=10, text= 'Close', command=root.destroy).place(x=240,y=150)




root.mainloop()
