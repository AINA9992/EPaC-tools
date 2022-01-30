import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import zipfile
import hashlib
import random
import string
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
    
    ####################
    # PASSWORD CRACKER #
    ####################
    def passwordCracker():
        def direction():
            dir.config(text = "This password cracking tool uses dictionary attack\n"
                    "It will only find password which is in the PassWordList.txt")
            ins.config(text ="Click browse for locked zip file to crack your locked zip file password.\n")
                
        def extractfile(zfile,password):
            try:
                zfile.extractall(pwd=bytes(password, 'utf-8'))
                return password
            except:
                print('Wrong password')
                return
  
        def checkpass():
            pswd.delete(0,END)
            # show the open file dialog
            filetypes = (
                ('zip files', '*.zip'),
                ('All files', '*.*')
            )
                
            filename = fd.askopenfilename( title='Open a file',
                initialdir='/',
                filetypes=filetypes)
            
            showinfo(
                title='Selected File',
                message= ("Click ok if the correct file path is shown.\n",filename)
                )
            zfile = zipfile.ZipFile(filename, 'r')
            passfile= open('PasswordList.txt')
            for line in passfile.readlines():
                password = line.strip('\n')
                guess = extractfile(zfile,password)
                if guess:
                    print('Your password = ' + password)
                    #Display password
                    lbl.config(text = "Your locked zip file password:" +password)
                    #pswd.insert(0,password)
                    
        # #Copy generated password to clipboard
        # def copypass():
        #     #Clear the clipboard
        #     root.copypass_clear()

        #     #compy to clipboard
        #     root.copypass_append(pswd.get())
            
        #Clear screen then call menu function/method
        def goback():
            dir.destroy()
            ins.destroy()
            lbl.destroy()
            pswd.destroy()
            button_checkpass.destroy()
            #button_copypass.destroy()
            button_goback.destroy()
            menu()
            
        #Clear screen by remove buttons and label
        l_name.destroy()
        button_pwCr.destroy()
        button_genPw.destroy()
        
        dir = tk.Label(root, text = "",font=("Arial",20),bd=0,bg="systembuttonface")
        dir.pack(pady=20)
        ins = tk.Label(root, text = "",font=("Arial",14),bd=0,bg="systembuttonface")
        ins.pack(pady=20)

        direction()
        
        # Label Creation
        lbl = tk.Label(root, text = "",font=("Arial",20),bd=0,bg="systembuttonface")
        lbl.pack(pady=20)
        
        #Entry box to display output password
        pswd = Entry(root,text=' ',font=("Arial",20),bd=0,bg="systembuttonface")
        pswd.pack(pady=20)
        
        #Button to check for password
        button_checkpass = Button(root,text="Browse for locked zip file",command=checkpass)
        button_checkpass.config(width=20,height=3,font=("Arial",10),bg="light blue")
        button_checkpass.pack(pady=5)

        # #Button copy the output of generated password
        # button_copypass = Button(root,text="Copy password to Clipboard",command=copypass)
        # button_copypass.config(width=20,height=3,font=("Arial",10),bg="light blue")
        # button_copypass.pack(pady=5)
            
        #Button to back to main
        button_goback = Button(root,text="Back to main menu",command=goback)
        button_goback.config(width=20,height=3,font=("Arial",10),bg="light blue")
        button_goback.pack(padx=5)
           
    #################
    # MENU FUNCTION #
    #################
    
    #Display title
    l_name = Label(root,text="\nEASY PASSWORD CRACKER (EPaC)\n",font=("Arial",30))
    l_name.pack(pady=20)

    #Button to go to password cracker function
    button_pwCr = Button(root,text="Password Cracker",command=passwordCracker)
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