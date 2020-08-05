from tkinter import *
from tkinter import ttk
import math,random
import os
import tkinter.messagebox as mb
from datetime import datetime  
import time

def total():    
    totalcprice=float((soap.get()*30)+(cream.get()*100)+(wash.get()*60)+(spray.get()*170)+(lotion.get()*180)+(shamp.get()*100))
    cprice.set("Rs. "+str(totalcprice))
    c=round((totalcprice*0.05),2)
    ctax.set("Rs. "+str(c))
    totalgprice=float((rice.get()*80)+(oil.get()*180)+(daal.get()*60)+(wheat.get()*240)+(sugar.get()*45)+(tea.get()*150))
    gprice.set("Rs. "+str(totalgprice))
    g=round((totalgprice*0.1),2)
    gtax.set("Rs. "+str(g)) 
    totalcdprice=float((pepsi.get()*45)+(frooti.get()*60)+(limca.get()*40)+(maaza.get()*50)+(fanta.get()*40)+(sprite.get()*60))
    cdprice.set("Rs. "+str(totalcdprice))
    cd=round((totalcdprice*0.05),2)
    cdtax.set("Rs. "+str(cd))

def wel():
    t.delete('1.0',END)
    t.insert(END,"              Welcome")
    t.insert(END,f"\n Bill  Number: {bill.get()}")
    t.insert(END,f"\n Customer Name: {cname.get()}")
    t.insert(END,f"\n Customer Phone No.:{cphone.get()}")
    t.insert(END,f"\n===============================")
    t.insert(END,f"\n Products      Qty        Price")
    t.insert(END,f"\n===============================")
def bil():
    if cname.get()==""or cphone.get()=="":
        mb.showerror("Error", "Customer Details Required")
    elif cprice.get()=="Rs 0.0" or  gprice.get()=="Rs 0.0" or cdprice.get()=="Rs 0.0":
        mb.showerror("Error", "No Item Selected")   
    else:
        wel()
        if soap.get()!=0:
            t.insert(END,f"\n Bath Soap:\t\t{soap.get()}\t  {soap.get()*30} ")
        if cream.get()!=0:
            t.insert(END,f"\n Face Cream:\t\t{cream.get()}\t  {cream.get()*100} ")   
        if wash.get()!=0:
            t.insert(END,f"\n Face Wash:\t\t{wash.get()}\t  {wash.get()*60} ")
        if spray.get()!=0:
            t.insert(END,f"\n Hair Spray:\t\t{spray.get()}\t  {spray.get()*170} ")
        if lotion.get()!=0:
            t.insert(END,f"\n Body Lotion:\t\t{lotion.get()}\t  {lotion.get()*180} ")
        if shamp.get()!=0:
            t.insert(END,f"\n Shampoo:\t\t{shamp.get()}\t  {shamp.get()*100} ")
        if rice.get()!=0:
            t.insert(END,f"\n Rice:\t\t{rice.get()}\t  {rice.get()*80} ")
        if oil.get()!=0:
            t.insert(END,f"\n Food Oil:\t\t{oil.get()}\t  {oil.get()*180} ")  
        if daal.get()!=0:
            t.insert(END,f"\n Daal:\t\t{daal.get()}\t  {daal.get()*60} ")
        if wheat.get()!=0:
            t.insert(END,f"\n Wheat:\t\t{wheat.get()}\t  {wheat.get()*240} ")
        if sugar.get()!=0:
            t.insert(END,f"\n Sugar:\t\t{sugar.get()}\t  {sugar.get()*45} ") 
        if tea.get()!=0:
            t.insert(END,f"\n Tea:\t\t{tea.get()}\t  {tea.get()*150} ")
        if pepsi.get()!=0:
            t.insert(END,f"\n Pepsi:\t\t{pepsi.get()}\t  {pepsi.get()*45} ")
        if frooti.get()!=0:
            t.insert(END,f"\n Frooti:\t\t{frooti.get()}\t  {frooti.get()*60} ")
        if limca.get()!=0:
            t.insert(END,f"\n Limca:\t\t{soap.get()}\t  {limca.get()*40} ") 
        if fanta.get()!=0:
            t.insert(END,f"\n Fanta:\t\t{fanta.get()}\t  {fanta.get()*40} ")
        if sprite.get()!=0:
            t.insert(END,f"\n Sprite:\t\t{sprite.get()}\t  {sprite.get()*60} ")
        if maaza.get()!=0:
            t.insert(END,f"\n Maaza: \t\t{maaza.get()}\t  {maaza.get()*50} ")  
        t.insert(END,f"\n-------------------------------")
        if ctax.get()!=0:
            t.insert(END,f"\n Cosmetic Tax: \t\t     {ctax.get()} ")
        if gtax.get()!=0:
            t.insert(END,f"\n Grocery Tax: \t\t      {gtax.get()} ")
        if cdtax.get()!=0:
            t.insert(END,f"\n Soft Drinks Tax: \t\t  {cdtax.get()} ")       
        t.insert(END,f"\n Total Bill:\t\t      Rs {float(soap.get()*30)+(cream.get()*100)+(wash.get()*60)+(spray.get()*170)+(lotion.get()*180)+(shamp.get()*100)+(rice.get()*80)+(oil.get()*180)+(daal.get()*60)+(wheat.get()*240)+(sugar.get()*45)+(tea.get()*150)+(pepsi.get()*45)+(frooti.get()*60)+(limca.get()*40)+(maaza.get()*50)+(fanta.get()*40)+(sprite.get()*60)}")         
        t.insert(END,f"\n-------------------------------")
        save() 
                                                         
def save():
    op=mb.askyesno("Save Bill","Do You Want To Save This Bill ") 
    if op==True:
        bills=t.get('1.0',END)
        f1=open("bills/"+str(bill.get())+".txt","w")
        f1.write(bills)
        f1.close()
        mb.showinfo("Saved",f"Bill no. {bill.get()} saved successfully")
    else:
        return    
def search():
    pre="no"
    for i in os.listdir("bills/"):
        if i.split('.')[0]==bill.get():
            f1=open(f"bills/{i}","r")
            t.delete('1.0',END)
            for d in f1:
                t.insert(END,d)
            f1.close()
            pre="yes"
    if pre=="no":
        mb.showerror("Error","Invalid Bill No.")         





def clr():
     op=mb.askyesno("Clear","Do u Really Want To Clear") 
     if op==True:
        soap.set("0")
        cream.set("0")
        wash.set("0")
        spray.set("0")
        lotion.set("0")
        shamp.set("0")
        rice.set("0")
        oil.set("0")
        daal.set("0")
        wheat.set("0")
        sugar.set("0")
        tea.set("0")
        pepsi.set("0")
        frooti.set("0")
        limca.set("0")
        maaza.set("0")
        fanta.set("0")
        sprite.set("0")
        cprice.set("")
        gprice.set("")
        cdprice.set("")
        ctax.set("")
        gtax.set("")
        cdtax.set("")
        cname.set("")
        cphone.set("")
        bill.set("")
        wel()
def exit():
    if cname.get()==""or cphone.get()=="":
        mb.showerror("Error", "Customer Details Required")
    elif cprice.get()=="Rs 0.0" or  gprice.get()=="Rs 0.0" or cdprice.get()=="Rs 0.0":
        mb.showerror("Error", "No Item Selected")   
    else:
        top.destroy()
        import pay
       
top=Tk()
top.title("Billing")
top.config(background="black")
top.geometry("1270x720+0+0")
top.resizable(0,0)
Label(top,text="Billing",fg="yellow",bg="#074463",bd=12,relief=GROOVE,font=("arial",30,"bold")).pack(fill=X)
soap=IntVar()
cream=IntVar()
wash=IntVar()
spray=IntVar()
lotion=IntVar()
shamp=IntVar()
rice=IntVar()
oil=IntVar()
daal=IntVar()
wheat=IntVar()
sugar=IntVar()
tea=IntVar()
pepsi=IntVar()
frooti=IntVar()
limca=IntVar()
maaza=IntVar()
fanta=IntVar()
sprite=IntVar()
cprice=StringVar()
gprice=StringVar()
cdprice=StringVar()
ctax=StringVar()
gtax=StringVar()
cdtax=StringVar()
cname=StringVar()
cphone=StringVar()
bill=StringVar()
x=random.randint(100,999)
bill.set(str(x))
d=StringVar()
t=StringVar()
d.set(time.strftime("%d:%m:%Y"))
t.set(time.strftime("%H:%M:%S"))
Label(top,textvariable=d,fg="white",bg="#074463",font=("arial",26,"bold")).place(x=30,y=13)
Label(top,textvariable=t,fg="white",bg="#074463",font=("arial",26,"bold")).place(x=1094,y=13)
f=LabelFrame(top,text="Customer Details",bg="#074463",fg="gold",bd=12,relief=GROOVE,font=("arial",15,"bold"))
f.place(x=0,y=75,relwidth=1)
Label(f,text="Customer Name",fg="white",bg="#074463",font=("arial",18,"bold"),padx=10).grid(row=0,column=0)
e1=Entry(f,width=15,font=("arial",18,"bold"),bd=7,textvariable=cname,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=10)
Label(f,text="Phone No.",fg="white",bg="#074463",font=("arial",18,"bold"),padx=10).grid(row=0,column=2)
e2=Entry(f,width=15,font=("arial",18,"bold"),bd=7,textvariable=cphone,relief=SUNKEN).grid(row=0,column=3,padx=5,pady=10)
Label(f,text="Bill No.",fg="white",bg="#074463",font=("arial",18,"bold"),padx=10).grid(row=0,column=4)
e3=Entry(f,width=15,font=("arial",18,"bold"),bd=7,textvariable=bill,relief=SUNKEN).grid(row=0,column=5,padx=5,pady=10)
Button(f,text="Search",command=search,fg="black",bg="white",font=("arial",17,"bold"),bd=7,relief=GROOVE,width=5,padx=5).grid(row=0,column=6)
f2=LabelFrame(top,text="Cosmetics",bg="#074463",fg="gold",bd=12,relief=GROOVE,font=("arial",15,"bold"))
f2.place(x=5,y=180,width=350,height=380)
Label(f2,text="Bath Soap",fg="lightgreen",bg="#074463",font=("arial",16,"bold"),padx=10).grid(row=0,column=0,padx=10,pady=10,sticky="w")
e4=Entry(f2,width=10,font=("arial",16,"bold"),bd=5,textvariable=soap,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
Label(f2,text="Face Cream",fg="lightgreen",bg="#074463",font=("arial",16,"bold"),padx=10).grid(row=1,column=0,padx=10,pady=10,sticky="w")
e5=Entry(f2,width=10,font=("arial",16,"bold"),textvariable=cream,bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
Label(f2,text="Face Wash",fg="lightgreen",bg="#074463",font=("arial",16,"bold"),padx=10).grid(row=2,column=0,padx=10,pady=10,sticky="w")
e6=Entry(f2,width=10,font=("arial",16,"bold"),textvariable=wash,bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
Label(f2,text="Hair Spray",fg="lightgreen",bg="#074463",font=("arial",16,"bold"),padx=10).grid(row=3,column=0,padx=10,pady=10,sticky="w")
e7=Entry(f2,width=10,font=("arial",16,"bold"),textvariable=spray,bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
Label(f2,text="Body Lotion",fg="lightgreen",bg="#074463",font=("arial",16,"bold"),padx=10).grid(row=4,column=0,padx=10,pady=10,sticky="w")
e8=Entry(f2,width=10,font=("arial",16,"bold"),textvariable=lotion,bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
Label(f2,text="Shampoo",fg="lightgreen",bg="#074463",font=("arial",16,"bold"),padx=10).grid(row=5,column=0,padx=10,pady=10,sticky="w")
e9=Entry(f2,width=10,font=("arial",16,"bold"),textvariable=shamp,bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
f3=LabelFrame(top,text="Grocery",bg="#074463",fg="gold",bd=12,relief=GROOVE,font=("arial",15,"bold"))
f3.place(x=360,y=180,width=310,height=380)
Label(f3,text="Rice",fg="lightgreen",bg="#074463",font=("arial",16,"bold"),padx=10).grid(row=0,column=0,padx=10,pady=10,sticky="w")
e10=Entry(f3,width=10,font=("arial",16,"bold"),textvariable=rice,bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
Label(f3,text="Food Oil",fg="lightgreen",bg="#074463",font=("arial",16,"bold"),padx=10).grid(row=1,column=0,padx=10,pady=10,sticky="w")
e11=Entry(f3,width=10,font=("arial",16,"bold"),textvariable=oil,bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
Label(f3,text="Daal",fg="lightgreen",bg="#074463",font=("arial",16,"bold"),padx=10).grid(row=2,column=0,padx=10,pady=10,sticky="w")
e12=Entry(f3,width=10,font=("arial",16,"bold"),textvariable=daal,bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
Label(f3,text="Wheat",fg="lightgreen",bg="#074463",font=("arial",16,"bold"),padx=10).grid(row=3,column=0,padx=10,pady=10,sticky="w")
e13=Entry(f3,width=10,font=("arial",16,"bold"),bd=5,textvariable=wheat,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
Label(f3,text="Sugar",fg="lightgreen",bg="#074463",font=("arial",16,"bold"),padx=10).grid(row=4,column=0,padx=10,pady=10,sticky="w")
e14=Entry(f3,width=10,font=("arial",16,"bold"),bd=5,textvariable=sugar,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
Label(f3,text="Tea",fg="lightgreen",bg="#074463",font=("arial",16,"bold"),padx=10).grid(row=5,column=0,padx=10,pady=10,sticky="w")
e15=Entry(f3,width=10,font=("arial",16,"bold"),textvariable=tea,bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
f4=LabelFrame(top,text="Soft Drinks",bg="#074463",fg="gold",bd=12,relief=GROOVE,font=("arial",15,"bold"))
f4.place(x=675,y=180,width=300,height=380)
Label(f4,text="Pepsi",fg="lightgreen",bg="#074463",font=("arial",16,"bold"),padx=10).grid(row=0,column=0,padx=10,pady=10,sticky="w")
e16=Entry(f4,width=10,font=("arial",16,"bold"),textvariable=pepsi,bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
Label(f4,text="Frooti",fg="lightgreen",bg="#074463",font=("arial",16,"bold"),padx=10).grid(row=1,column=0,padx=10,pady=10,sticky="w")
e17=Entry(f4,width=10,font=("arial",16,"bold"),bd=5,textvariable=frooti,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
Label(f4,text="Limca",fg="lightgreen",bg="#074463",font=("arial",16,"bold"),padx=10).grid(row=2,column=0,padx=10,pady=10,sticky="w")
e18=Entry(f4,width=10,font=("arial",16,"bold"),bd=5,textvariable=limca,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
Label(f4,text="Fanta",fg="lightgreen",bg="#074463",font=("arial",16,"bold"),padx=10).grid(row=3,column=0,padx=10,pady=10,sticky="w")
e19=Entry(f4,width=10,font=("arial",16,"bold"),bd=5,textvariable=fanta,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
Label(f4,text="Sprite",fg="lightgreen",bg="#074463",font=("arial",16,"bold"),padx=10).grid(row=4,column=0,padx=10,pady=10,sticky="w")
e20=Entry(f4,width=10,font=("arial",16,"bold"),bd=5,textvariable=sprite,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
Label(f4,text="Maaza",fg="lightgreen",bg="#074463",font=("arial",16,"bold"),padx=10).grid(row=5,column=0,padx=10,pady=10,sticky="w")
e21=Entry(f4,width=10,font=("arial",16,"bold"),bd=5,textvariable=maaza,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
f5=Frame(top,bd=12,relief=GROOVE)
f5.place(x=975,y=180,width=300,height=385)
Label(f5,text="Bill Area",fg="black",font=("arial",15,"bold"),bd=7,relief=GROOVE).pack(fill=X)
scroll=Scrollbar(f5,orient=VERTICAL)
t=Text(f5,yscrollcommand=scroll.set)
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=t.yview)
t.pack(fill=BOTH,expand=1)
f6=LabelFrame(top,text="Bill Menu",bg="#074463",fg="gold",bd=12,relief=GROOVE,font=("arial",15,"bold"))
f6.place(x=0,y=565,relwidth=1,height=165)
Label(f6,text="Total Cosmetic Price",fg="white",bg="#074463",font=("arial",13,"bold"),padx=2).grid(row=0,column=0,padx=10,pady=10,sticky="w")
e22=Entry(f6,width=10,textvariable=cprice,font=("arial",12,"bold"),bd=4,relief=SUNKEN).grid(row=0,column=1,padx=10,sticky="w")
Label(f6,text="Total Grocery Price",fg="white",bg="#074463",font=("arial",13,"bold"),padx=2).grid(row=1,column=0,padx=10,pady=10,sticky="w")
e23=Entry(f6,width=10,textvariable=gprice,font=("arial",12,"bold"),bd=4,relief=SUNKEN).grid(row=1,column=1,padx=10,sticky="w")
Label(f6,text="Total Soft Drinks Price",fg="white",bg="#074463",font=("arial",13,"bold"),padx=2).grid(row=2,column=0,padx=10,pady=10,sticky="w")
e24=Entry(f6,width=10,textvariable=cdprice,font=("arial",12,"bold"),bd=4,relief=SUNKEN).grid(row=2,column=1,padx=10,sticky="w")
Label(f6,text="Cosmetic Tax",fg="white",bg="#074463",font=("arial",13,"bold"),padx=2).grid(row=0,column=3,padx=10,pady=10,sticky="w")
e25=Entry(f6,width=10,textvariable=ctax,font=("arial",12,"bold"),bd=4,relief=SUNKEN).grid(row=0,column=4,padx=10,sticky="w")
Label(f6,text="Grocery Tax",fg="white",bg="#074463",font=("arial",13,"bold"),padx=2).grid(row=1,column=3,padx=10,pady=10,sticky="w")
e26=Entry(f6,width=10,textvariable=gtax,font=("arial",12,"bold"),bd=4,relief=SUNKEN).grid(row=1,column=4,padx=10,sticky="w")
Label(f6,text="Soft Drinks Tax",fg="white",bg="#074463",font=("arial",13,"bold"),padx=2).grid(row=2,column=3,padx=10,pady=10,sticky="w")
e27=Entry(f6,width=10,textvariable=cdtax,font=("arial",12,"bold"),bd=4,relief=SUNKEN).grid(row=2,column=4,padx=10,sticky="w")
Button(top,text="Total",command=total,fg="black",bg="cadetblue",font=("arial",20,"bold"),bd=7,relief=GROOVE,padx=10).place(x=610,y=618)
Button(top,text="Generate Bill",command=bil,fg="black",bg="cadetblue",font=("arial",20,"bold"),bd=7,relief=GROOVE,padx=10).place(x=750,y=618)
Button(top,text="Clear",command=clr,fg="black",bg="cadetblue",font=("arial",20,"bold"),bd=7,relief=GROOVE,padx=10).place(x=990,y=618)
Button(top,text="Pay",command=exit,fg="black",bg="cadetblue",font=("arial",20,"bold"),bd=7,relief=GROOVE,padx=10).place(x=1130,y=618)
wel()
top.mainloop()
