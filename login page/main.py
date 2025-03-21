from tkinter import *
import sqlite3
root=Tk()
root.geometry('600x500')
root.title("RESISTRATION")
fname=StringVar()
Email=StringVar()
var=IntVar(),
c=StringVar()
var1=IntVar()

def database():
    name=fname.get()
    email=Email.get()
    gender=var1.get()
    country=c.get()
    prog=var1.get()
    conn=sqlite3.connect('form2.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Student(fname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)')
    cursor.execute('INSERT INTO Student(fname,Email,Gender,country,Programming)VALUES(?,?,?,?,?)',[name,email,gender,country,prog],)
    conn.commit()
l1=Label(root,text="REGISTRATION FORM",width=40,fg="red",font="bold")
l1.place(x=120,y=53)

l2=Label(root,text="FULL NAME",width=20)
l2.place(x=70,y=100)
entry=Entry(root,textvar=fname)
entry.place(x=190,y=100)

l3=Label(root,text="Email",width=20)
l3.place(x=60,y=150)
entry=Entry(root,textvar=Email)
entry.place(x=190,y=150)

l4=Label(root,text="Gender",width=20)
l4.place(x=60,y=200)
Radiobutton(root,text="Male",padx=5,variable=var,value=1).place(x=180,y=200)
Radiobutton(root,text="female",padx=10,variable=var,value=2).place(x=270,y=200)

l5=Label(root,text="Location",width=20).place(x=60,y=250)
list1=["Noida ","Banglore","Pune","USA","Gurugram"]
droplist=OptionMenu(root,c,*list1)
droplist.config(width=15)
c.set('select your Location')
droplist.place(x=180,y=240)

l6=Label(root,text="Programming",width=20)
l6.place(x=60,y=290)
var2=IntVar()
Checkbutton(root,text="java",variable=var1).place(x=200,y=290)
Checkbutton(root,text="Python",variable=var2).place(x=290,y=290)
Button(root,text="SUBMIT",width=20,fg="black",command=database).place(x=150,y=350)
root.mainloop()


