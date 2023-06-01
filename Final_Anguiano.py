from tkinter import *
from tkinter import messagebox
from math import *



root = Tk()
root.title('Fourier Series')
root.geometry('1220x620')
root.resizable(width=False, height=False)


    
#define class and constructor 
class show():
    def __init__(self,function):
        if function == '':
            messagebox.showerror('error','please enter a function')
            exit()
        else:
            self.f=eval('lambda x:'+function)
        self.a0,self.mx,self.mi=self.integral()
        self.fx=lambda x: round(600*(x+3*pi)/(6*pi))+54
        self.fy=lambda y: round(350*(self.mx-y)/(self.mx-self.mi))+54

    #integral method
    def integral(self,funcn=''):
        f=funcn if funcn else self.f
        n=10000
        dx=pi/5000
        fx=[f(-pi+i*dx) for i in range(n+1)]
        intgl=(dx/3)*(fx[0]+4*sum(fx[1:n:2])+2*sum(fx[2:n:2])+fx[n])
        if not funcn:
            mx=round(max(fx))+0.5
            mi=round(min(fx))-0.5
            intgl=[intgl,mx,mi]
        return intgl

    #coord() method
    def coord(self):
        p.create_line(12,self.fy(0),702,self.fy(0),width=1,arrow=LAST)
        p.create_line(self.fx(0),452,self.fx(0),12,width=1,arrow=LAST)
        tx=0.5
        while tx*pi<=3*pi:
            p.create_line(self.fx(tx*pi),self.fy(0),self.fx(tx*pi),self.fy(0)+5,width=1)
            p.create_text(self.fx(tx*pi),self.fy(0)+6,anchor=N,text=str(tx)+'\u03C0')
            tx=tx+0.5
        tx=-0.5
        while tx*pi>=-3*pi:
            p.create_line(self.fx(tx*pi),self.fy(0),self.fx(tx*pi),self.fy(0)+5,width=1)
            p.create_text(self.fx(tx*pi),self.fy(0)+6,anchor=N,text=str(tx)+'\u03C0')
            tx=tx-0.5
        ty=0.5
        while ty<=self.mx:
            p.create_line(self.fx(0),self.fy(ty),self.fx(0)-5,self.fy(ty),width=1)
            p.create_text(self.fx(0)-6,self.fy(ty),anchor=E,text=str(ty))
            ty=ty+0.5
        ty=-0.5
        while ty>=self.mi:
            p.create_line(self.fx(0),self.fy(ty),self.fx(0)-5,self.fy(ty), width=1)
            p.create_text(self.fx(0)-6,self.fy(ty),anchor=E,text=str(ty))
            ty=ty-0.5


    #plotf() Method
    def plotf(self,color,sm,fn=''):
        if not fn:  fn=self.f
        pts=sum([[self.fx(-3.5*pi+i*7*pi/1000),self.fy(fn(-3.5*pi+i*7*pi/1000))]
                 for i in range(1001)],[])
        p.create_line(*pts, width=3, fill=color,smooth=sm)

    #Fourier() Method
    def fourier(self):
        a0=self.a0/(2*pi)
        a=[self.integral(lambda x:self.f(x)*cos(i*x)/pi)
           for i in range(1,21)]
        b=[self.integral(lambda x:self.f(x)*sin(i*x)/pi)
           for i in range(1,21)]
        return a0,a,b

    #partialfs() Method
    def partialfs(self,n):
        a0,a,b=self.fourier()
        fs=lambda x:a0+sum([a[i-1]*cos(i*x)+b[i-1]*sin(i*x) for i in range(n+1)])
        return fs

    #fourierstr() Method
    def fourierstr(self):
        a0,a,b=self.fourier()
        fstr=''
        if abs(a0)>1e-10:
            fstr=fstr+str(a0)+'\n'
        if (abs(a[0])>1e-10 and abs(b[0])>1e-10):
            fstr=fstr+str(a[0])+'*cos(x)+'+str(b[0])+'*sin(x)+\n'
        elif abs(a[0])>1e-10:
            fstr=fstr+'+'+str(a[0])+'*cos(x)+\n'
        elif abs(b[0])>1e-10:
            fstr=fstr+'+'+str(b[0])+'*sin(x)+\n'
        else:
            pass
        for i in range(2,21):
            if (abs(a[i-1])>1e-10 and abs(b[i-1])>1e-10):
                fstr=fstr+(str(a[i-1])+'*cos('+str(i)+'x)+'+str(b[i-1])+'*sin('+str(i)+'x)+\n')
            elif abs(a[i-1])>1e-10:
                fstr=fstr+str(a[i-1])+'*cos('+str(i)+'x)+\n'
            elif abs(b[i-1])>1e-10:
                fstr=fstr+str(b[i-1])+'*sin('+str(i)+'x)+\n'
            else:
                pass
        fstr=fstr+'......'
        return fstr

#Series() function
def series():
    f=fn.get()
    window=show(f)
    txt=window.fourierstr()
    t.delete(1.0,END)
    t.insert(1.0, txt)

#plot() function
def plot():
    p.delete('all')
    f=fn.get()
    window=show(f)
    window.coord()
    if Checkfn.get()==1:
        window.plotf('red',0)
    if Checksr.get()==1:
        c=color.get()
        m=nvar.get()
        fs=window.partialfs(m)
        window.plotf(c,1,fs)

#add() function
def add(event):
    f=fn.get()
    if Checksr.get()==1:
        c=ctuple[(ctuple.index(color.get())+1)%16]
        m=nvar.get()
        color.set(c)
        window=show(f)
        fs=window.partialfs(m)
        window.plot(c,1,fs)

#clear() function
def clear():
    p.delete('all')
    t.delete(1.0,END)
    fn.set('')
    n.set(1)
    Checkfn.set(0)
    Checksr.set(0)
    



        
    
    
        
        
        
        
    
fn=StringVar()
Checkfn=IntVar()
Checksr=IntVar()
nvar=IntVar()
color=StringVar()


        



#frameA
frameA=Frame(root)
frameA.pack()

#frame1
frame1=Frame(frameA)
frame1.pack(side=LEFT,padx=20,fill=Y)
p=Canvas(frame1,bg='white',width=700,height=450,relief=SUNKEN, bd=5)
p.pack(pady=20)

#frame2
frame2=Frame(frameA)
frame2.pack(side=LEFT,fill=Y)

#frame2a
frame2a=Frame(frame2)
frame2a.pack()
Label(frame2a,text='The Fourier series of a periodic function f(x) of period 2'
      + '\u03C0'+'is',font=('Arial',10)).pack(side=LEFT,padx=(0,100),pady=10)

#frame2b
frame2b=Frame(frame2)
frame2b.pack()
canvas1 = Canvas(frame2b,width=245, height=47, bg='white')
canvas1.pack()
gif1 = PhotoImage(file='finala.gif')
canvas1.create_image(0,0, image=gif1,anchor=NW)


#frame2c
frame2c=Frame(frame2)
frame2c.pack()
Label(frame2c,text='where',font=('Arial',10)).pack(side=LEFT, padx=(0,400))

#frame2d
frame2d=Frame(frame2)
frame2d.pack()
canvas2 = Canvas(frame2d,width=370, height=48, bg='white')
canvas2.pack()
gif2 = PhotoImage(file='finalb.gif')
canvas2.create_image(0,0, image=gif2,anchor=NW)

#frame2e
frame2e=Frame(frame2)
frame2e.pack(pady=(10,0))
Label(frame2e,text='Enter a periodic function of period 2' + '\u03C0'
      +':',font=('Arial',10)).pack(padx=(0,200),pady=(10,0))

#frame2f
frame2f=Frame(frame2)
frame2f.pack()
Label(frame2f,text='f(x)=',font=('Arial Bold',12)).pack(side=LEFT, padx=(20,0), pady=10)
Entry(frame2f, width=55,textvariable=fn).pack(side=RIGHT)

#frame2g
frame2g=Frame(frame2)
frame2g.pack(pady=(10,0))
Label(frame2g,text='Compare the first 20 terms of the Fourier series',font=('Arial',10)).pack(side=LEFT,padx=(0,10))
btn1 = Button(frame2g, width=10, text='compute',font=('Arial Bold',10),command=series)
btn1.pack(side=LEFT, padx=(10,0))

#frame2h
frame2h=Frame(frame2)
frame2h.pack(pady=20)
s=Scrollbar(frame2h)
t=Text(frame2h,height=10,width=60,font=('Arial',10))
s.pack(side=RIGHT,fill=Y)
t.pack(side=LEFT,fill=Y)
s.config(command=t.yview)
t.config(yscrollcommand=s.set)

#frameB
frameB=Frame(root)
frameB.pack()
Label(frameB,text='Graphs:',font=('Arial Bold',10)
      ).grid(row=0,column=0,padx=(0,15))
Checkbutton(frameB, text='Function',font=('Arial',10),
            onvalue=1,offvalue=0,variable=Checkfn).grid(row=0,column=1,padx=(15,15))
Checkbutton(frameB, text='Partial Fourier Series', font=('Arial',10),
             onvalue=1,offvalue=0,variable=Checksr).grid(row=0,column=2,padx=(15,15))
n=Scale(frameB,from_=1,to=20,tickinterval= 2,label='Number of the terms:',orient=HORIZONTAL,length=350,showvalue=1,resolution=1,font=('Arial', 10),variable=nvar)
n.grid(row=0,column=3,padx=(15,15))
n.bind('<ButtonRelease-1>',add)
Label(frameB,text='Color:',font=('Arial', 10)).grid(row=0,column=4,padx=(10,5))
ctuple=('blue','orange','chocolate1','dark green','deep pink',
'blue violet','goldenrod','cyan2','tan1','turquoise1',
'magenta2','green','SlateBlue1','yellow','lawn green',
'dark salmon')
Spinbox(frameB,values=ctuple,width=10,textvariable=color).grid(row=0,column=5,padx=(5,10))
btn2=Button(frameB,width=10,text='Plot',font=('Arial Bold',10),command=plot)
btn2.grid(row=0,column=6,padx=(10,20))
btn3=Button(frameB,width=10,text='Clear',font=('Arial Bold',10),command=clear)
btn3.grid(row=0,column=7,padx=(20,0))



#tests





root.mainloop()





