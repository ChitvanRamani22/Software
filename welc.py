from tkinter import *
import tkinter.messagebox as mb
import mysql.connector
from PIL import Image, ImageTk
def ch():
    conn=mysql.connector.connect(host="localhost",user="root",password="",database="rest")
    csr=conn.cursor()
    user=(e1.get())
    pwd=(e2.get())
    csr.execute("select * from login where usr='"+user+"' and pwd='"+pwd+"'")
    if(csr.fetchone()):
        top.destroy()
        import bill
    else:    
        mb.showinfo("Retry","Email or Password is incorrect")
def chi():
    top.destroy()
    import wel

top=Tk()
top.title("WELCOME")
top.config(background="black")
top.geometry("600x450+100+100")
top.resizable(0,0)
image=Image.open("gt.jpg")
pho=ImageTk.PhotoImage(image)
r=Label(top,image=pho,bg="black")
r.place(x=0,y=0)
Label(top,text="LOGIN",fg="black",bg="yellow",font=("arial",40,"bold"),bd=7,relief=GROOVE).place(x=330,y=40)
l=Label(top,text="USER ID",bg="yellow",fg="blue",borderwidth=4,relief=SUNKEN,width=10,font=("arial",16))
l.place(x=240,y=150)
l=Label(top,text="Password",bg="yellow",fg="blue",borderwidth=4,relief=SUNKEN,width=10,font=("arial",16))
l.place(x=240,y=220)
e1=Entry(top,width="14",font=("arial",18))
e1.place(x=380,y=151)
e2=Entry(top,show="*",width="14",font=("arial",18))
e2.place(x=380,y=221)
Button(top,text="Sign In",fg="yellow",bg="red",font=("arial",15),borderwidth=4,relief=SUNKEN,command=ch).place(x=320,y=300)
Button(top,text="Cancel",fg="yellow",bg="red",font=("arial",15),borderwidth=4,relief=SUNKEN,command=chi).place(x=420,y=300)
top.mainloop()