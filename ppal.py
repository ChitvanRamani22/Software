from tkinter import *
import mysql.connector
from PIL import Image, ImageTk
import tkinter.messagebox as mb
OptionList = [
"Albenia",
"Australia",
"Brazil",
"Cananda",
"Columbia",
"Denmark",
"Egypt",
"France",
"Germany",
"Hong Kong",
"India",
"Japan",
"Kenya",
"Netherlands"
"Mexico",
"Nigeria",
"Russia",
"Switzerland",
"Zimbabwe"
] 
def exit():
    if lname.get()=="" or cname.get()=="" or ad.get()=="" or cty.get()=="" or ste.get()=="" or em.get()=="":
        mb.showerror("Error", "Customer Details Required")
    elif zc.get()==0:
        mb.showerror("Error", "Zip Code Required") 
    else:  
        conn=mysql.connector.connect(host="localhost",user="root",password="",database="rest")
        csr=conn.cursor()
        csr.execute("insert into paypal(first_name,last_name,email,address,city,state,country,zip_code) values('"+str(cname.get())+"','"+str(lname.get())+"','"+str(em.get())+"','"+str(ad.get())+"','"+str(cty.get())+"','"+str(ste.get())+"','"+str(app.get())+"','"+str(zc.get())+"')")
        conn.commit()   
        lname.set("")
        cty.set("")
        ste.set("")
        ad.set("")
        zc.set("0")
        em.set("")
        cname.set("") 
        top.destroy()
        import success
top=Tk()
top.title("Debit Card")
top.config(background="white")
top.geometry("630x630+330+10")
top.resizable(0,0)
image=Image.open("hr.jpg")
pho=ImageTk.PhotoImage(image)
r=Label(top,image=pho)
r.pack()
f3=Frame(top,bg="white",bd=12,relief=GROOVE)
f3.place(x=55,y=15,width=520,height=600)
Label(f3,text="PayPal Payment",fg="green",bg="white",font=("arial",20,"bold")).place(x=140,y=10)
zc=IntVar()
lname=StringVar()
em=StringVar()
cname=StringVar()
cty=StringVar()
ste=StringVar()
ad=StringVar()
app=StringVar()
app.set("Select  Country")
Label(f3,text="FIRST NAME",fg="black",bg="white",font=("arial",14,"bold")).place(x=20,y=60)
e3=Entry(f3,width=35,font=("arial",16,"bold"),bd=5,relief=SUNKEN,textvariable=cname)
e3.place(x=20,y=90)
Label(f3,text="LAST NAME",fg="black",bg="white",font=("arial",14,"bold")).place(x=20,y=130)
e4=Entry(f3,width=35,font=("arial",16,"bold"),bd=5,relief=SUNKEN,textvariable=lname)
e4.place(x=20,y=160)
Label(f3,text="EMAIL ADDRESS",fg="black",bg="white",font=("arial",14,"bold")).place(x=20,y=200)
e5=Entry(f3,width=35,font=("arial",16,"bold"),bd=5,relief=SUNKEN,textvariable=em)
e5.place(x=20,y=230)
Label(f3,text="ADDRESS",fg="black",bg="white",font=("arial",14,"bold")).place(x=20,y=270)
e6=Entry(f3,width=35,font=("arial",16,"bold"),bd=5,relief=SUNKEN,textvariable=ad)
e6.place(x=20,y=300)
Label(f3,text="CITY",fg="black",bg="white",font=("arial",14,"bold")).place(x=20,y=340)
e7=Entry(f3,width=15,font=("arial",16,"bold"),bd=5,relief=SUNKEN,textvariable=cty)
e7.place(x=20,y=370)
Label(f3,text="STATE",fg="black",bg="white",font=("arial",14,"bold")).place(x=220,y=340)
e8=Entry(f3,width=18,font=("arial",16,"bold"),bd=5,relief=SUNKEN,textvariable=ste)
e8.place(x=220,y=370)
Label(f3,text="ZIP CODE",fg="black",bg="white",font=("arial",14,"bold")).place(x=20,y=410)
e9=Entry(f3,width=15,font=("arial",16,"bold"),bd=5,relief=SUNKEN,textvariable=zc)
e9.place(x=20,y=440)
opt = OptionMenu(f3, app, *OptionList)
opt.config(width=20, font=('aerial', 13,"bold"),bg="lightgreen")
opt.place(x=220,y=440)
Checkbutton(f3,text="By checking this box, I agree the Terms & Conditions & Privacy Policy",bg="white",fg="black",font=("arial",10,"bold")).place(x=12,y=480)
Button(f3,text="SUBMIT",command=exit,fg="white",bg="green",font=("arial",18,"bold"),bd=5,relief=GROOVE).place(x=170,y=515)
top.mainloop()