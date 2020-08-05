from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as mb
import mysql.connector
def exit():
    if fnme.get()=="":
        mb.showerror("Error", "Customer Details Required")
    elif cname.get()=="" or  cv.get()==0 or yr.get()==0 or da.get()==0 or crdn.get()==0:
        mb.showerror("Error", "Card Details Required")  
    elif len(str(crdn.get()))!=16:
         mb.showerror("Error", "Invalid Card Number")  
    else:
        conn=mysql.connector.connect(host="localhost",user="root",password="",database="rest")
        csr=conn.cursor()
        csr.execute("insert into credit(email,first_name,card_name,card_number,date,year,cvv) values('"+str(em.get())+"','"+str(fnme.get())+"','"+str(cname.get())+"','"+str(crdn.get())+"','"+str(da.get())+"','"+str(yr.get())+"','"+str(cv.get())+"')")
        conn.commit()
        cv.set("0")
        crdn.set("0")
        da.set("0")
        yr.set("0")
        fnme.set("")
        em.set("")
        cname.set("") 
        top.destroy()
        import success
top=Tk()
top.title("Credit Card")
top.config(background="white")
top.geometry("630x630+330+10")
top.resizable(0,0)
image=Image.open("hr.jpg")
pho=ImageTk.PhotoImage(image)
r=Label(top,image=pho)
r.pack()
f3=Frame(top,bg="white",bd=12,relief=GROOVE)
f3.place(x=55,y=15,width=520,height=600)
Label(f3,text="Personal Information",fg="green",bg="white",font=("arial",20,"bold")).place(x=110,y=10)
cv=StringVar()
crdn=StringVar()
da=IntVar()
yr=IntVar()
fnme=StringVar()
em=StringVar()
cname=StringVar()
Label(f3,text="EMAIL ADDRESS",fg="black",bg="white",font=("arial",14,"bold")).place(x=20,y=60)
e3=Entry(f3,width=35,font=("arial",16,"bold"),bd=5,relief=SUNKEN,textvariable=em)
e3.place(x=20,y=90)
Label(f3,text="FIRST NAME",fg="black",bg="white",font=("arial",14,"bold")).place(x=20,y=130)
e4=Entry(f3,width=35,font=("arial",16,"bold"),bd=5,relief=SUNKEN,textvariable=fnme)
e4.place(x=20,y=160)
Label(f3,text="Credit Card Info",fg="green",bg="white",font=("arial",20,"bold")).place(x=145,y=210)
Label(f3,text="NAME ON CARD",fg="black",bg="white",font=("arial",14,"bold")).place(x=20,y=260)
e5=Entry(f3,width=35,font=("arial",16,"bold"),bd=5,relief=SUNKEN,textvariable=cname)
e5.place(x=20,y=290)
Label(f3,text="CARD NUMBER",fg="black",bg="white",font=("arial",14,"bold")).place(x=20,y=330)
e6=Entry(f3,width=35,font=("arial",16,"bold"),bd=5,relief=SUNKEN,textvariable=crdn)
e6.place(x=20,y=360)
Label(f3,text="EXPIRATION",fg="black",bg="white",font=("arial",14,"bold")).place(x=20,y=400)
e7=Entry(f3,width=8,font=("arial",16,"bold"),bd=5,relief=SUNKEN,textvariable=da)
e7.place(x=20,y=430)
e8=Entry(f3,width=8,font=("arial",16,"bold"),bd=5,relief=SUNKEN,textvariable=yr)
e8.place(x=130,y=430)
Label(f3,text="CVV NUMBER",fg="black",bg="white",font=("arial",14,"bold")).place(x=285,y=400)
e9=Entry(f3,width=15,font=("arial",16,"bold"),bd=5,relief=SUNKEN,textvariable=cv,show="*")
e9.place(x=285,y=430)
Checkbutton(f3,text="By checking this box, I agree the Terms & Conditions & Privacy Policy",bg="white",fg="black",font=("arial",10,"bold")).place(x=12,y=480)
Button(f3,text="SUBMIT",command=exit,fg="white",bg="green",font=("arial",18,"bold"),bd=5,relief=GROOVE).place(x=170,y=515)
top.mainloop()