import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import zipfile
import hashlib
import random
import string

root = Tk()

root.geometry("1000x500")

l_name = Label(root,text="PASSWORD CRACKER\n",font=("Arial",30))
l_name.pack(pady=20)

text = tk.Text(root, height=12)

def extractfile(zfile,password):
    try:
        zfile.extractall(pwd=bytes(password, 'utf-8'))
        return password
    except:
        print('Wrong password')
        return

def main():
    #Label frame
    lf = LabelFrame(root,text="Enter the locked zip file name: \n"
                    "Please include extension which is .zip"
                 " at the end of the file name): ")
    lf.pack(pady=20)
    
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
        message=filename
    )
    zfile = zipfile.ZipFile(filename, 'r')
    passfile= open('PasswordList.txt', errors='ignore')
    for line in passfile.readlines():
        password = line.strip('\n')
        guess = extractfile(zfile,password)
        if guess:
            print('Your password = ' + password)
            pswd = Entry(root,text='',font=("Arial",20),bd=0,bg="systembuttonface")
            pswd.pack(pady=20)
            #Entry box to display output password that has been generated
            pswd.insert(0,password)
        
if __name__=='__main__':
    main()
    
#Execute Tkinter
root.mainloop()