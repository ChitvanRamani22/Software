'''from tkinter import *
top=Tk()
top.title("WELCOME")
top.config(background="black")
top.geometry("600x700+100+100")
top.resizable(0,0)
photo=PhotoImage(file="r.png")
r=Label(top,image=photo)
r.pack()
top.mainloop()'''
from tkinter import *
from PIL import Image, ImageTk
def ch():
    top.destroy()
    import welc
top=Tk()
top.title("WELCOME")
top.config(background="black")
top.geometry("1255x695+5+0")
top.resizable(0,0)
image=Image.open("se.jpg")
pho=ImageTk.PhotoImage(image)
r=Label(top,image=pho)
r.pack()
Button(top,text="ENTER",fg="black",bg="cadetblue",font=("arial",25),borderwidth=7,relief=GROOVE,command=ch).place(x=280,y=560)
top.mainloop()