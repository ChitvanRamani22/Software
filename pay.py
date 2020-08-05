from tkinter import *

from PIL import Image, ImageTk
def cre():
    top.destroy()
    import credit
def pal():
    top.destroy()
    import ppal 
def deb():
    top.destroy()
    import debit          
top=Tk()
top.title("WELCOME")
top.config(background="white")
top.geometry("1005x580+150+30")
top.resizable(0,0)
image=Image.open("sre.jpg")
pho=ImageTk.PhotoImage(image)
r=Label(top,image=pho)
r.pack()
Label(top,text="Select Payment Method",fg="black",bg="yellow",font=("timesnew roman",24)).place(x=335,y=40)
photo=PhotoImage(file="c.png")
t=Label(top,image=photo)
t.place(x=40,y=170)
phot=PhotoImage(file="d.png")
s=Label(top,image=phot)
s.place(x=730,y=170)
ph=PhotoImage(file="gt.png")
e=Label(top,image=ph,height=250,width=250)
e.place(x=380,y=155)
Button(top,text="Credit Card",fg="black",font=("arial",20,"bold"),bd=5,bg="cadetblue",relief=GROOVE,command=cre).place(x=60,y=440)
Button(top,text="PayPal ",fg="black",font=("arial",20,"bold"),bd=5,bg="cadetblue",relief=GROOVE,command=pal).place(x=445,y=440)
Button(top,text="Debit Card",fg="black",font=("arial",20,"bold"),bd=5,bg="cadetblue",relief=GROOVE,command=deb).place(x=765,y=440)
top.mainloop()
