from tkinter import *
from tkinter import ttk
from random import randint

root=Tk()
root.geometry("1000x500")

def menu():
    #Display title
    l_name = Label(root,text="\nEASY PASSWORD CRACKER (EPaC)\n",font=("Arial",30))
    l_name.pack(pady=20)

    #Display frame
    frame.pack(pady=20)

    #Button to go to password cracker function
    button_pwCr = Button(frame,text="Password Cracker") #,command=passwordCracker fx )
    button_pwCr.config(width=25,height=5,font=("Arial",15),bg="light blue")
    button_pwCr.grid(row=0,column=0,pady=10,padx=20)
    
    #Button to go to password generator function
    button_genPw = Button(frame,text="Strong Password Generator") #,command=generatePw fx )
    button_genPw.config(width=25,height=5,font=("Arial",15),bg="light blue")
    button_genPw.grid(row=0,column=1,pady=10,padx=20)

frame = Frame(root)

#Call menu function
menu()

#Execute Tkinter
root.mainloop()