from tkinter import *
from tkinter import ttk
from random import randint

def menu():     

    #Strong password generator
    def genPw():

        #Generate random password
        def new_rand():
            #Clear entry box
            generated_pw.delete(0,END)

            #Get password length and convert to integer
            pwLength = int(num_char.get())
    
            #Variable to hold the password
            pw = ''

            #Loop through password length
            for x in range(pwLength):
                pw += chr(randint(33,126))

            #Display password that has been generated
            generated_pw.insert(0,pw)

        #Copy generated password to clipboard
        def clipper():
            #Clear the clipboard
            root.clipboard_clear()

            #compy to clipboard
            root.clipboard_append(generated_pw.get())
        
        #Clear screen then call menu function/method
        def back():
            l_frame.destroy()
            generated_pw.destroy()
            num_char.destroy()
            button_gen.destroy()
            button_clip.destroy()
            button_back.destroy()
            menu()
        
        ######################################
        # STRONG PASSWORD GENERATOR FUNCTION #
        ######################################

        #Clear screen by remove buttons and label
        l_name.destroy()
        button_pwCr.destroy()
        button_genPw.destroy()
            
        #Label frame
        l_frame = LabelFrame(root,text="How many characters?")
        l_frame.pack(pady=20)

        #Entry box to accept input number of characters to generate
        num_char = Entry(l_frame,font=("Arial",20))
        num_char.pack(pady=20,padx=20)

        #Entry box to display output password that has been generated
        generated_pw = Entry(root,text='',font=("Arial",20),bd=0,bg="systembuttonface")
        generated_pw.pack(pady=20)
        
        #Button to generate password
        button_gen = Button(root,text="Go",command=new_rand)
        button_gen.config(width=20,height=3,font=("Arial",10),bg="light blue")
        button_gen.pack(pady=5)

        #Button copy the output of generated password
        button_clip = Button(root,text="Copy to Clipboard",command=clipper)
        button_clip.config(width=20,height=3,font=("Arial",10),bg="light blue")
        button_clip.pack(pady=5)
            
        #Button to back to main
        button_back = Button(root,text="Back to menu",command=back)
        button_back.config(width=20,height=3,font=("Arial",10),bg="light blue")
        button_back.pack(padx=5)
    
    #################
    # MENU FUNCTION #
    #################
    
    #Display title
    l_name = Label(root,text="\nEASY PASSWORD CRACKER (EPaC)\n",font=("Arial",30))
    l_name.pack(pady=20)

    #Button to go to password cracker function
    button_pwCr = Button(root,text="Password Cracker") #,command=passwordCracker fx )
    button_pwCr.config(width=25,height=3,font=("Arial",15),bg="light blue")
    button_pwCr.pack(pady=5)
    
    #Button to go to password generator function
    button_genPw = Button(root,text="Strong Password Generator",command=genPw)
    button_genPw.config(width=25,height=3,font=("Arial",15),bg="light blue")
    button_genPw.pack(pady=5)

root=Tk()
root.geometry("1000x500")
#Call menu function
menu()

#Execute Tkinter
root.mainloop()