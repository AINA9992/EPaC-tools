from tkinter import *
import zipfile
import hashlib
import random
import string

root = Tk()

l_name = Label(root,text="PASSWORD CRACKER\n",font=("Arial",15))
l_name.pack(pady=20)

def extractfile(zfile,password):
    try:
        zfile.extractall(pwd=bytes(password, 'utf-8'))
        return password
    except:
        print('Password failed')
        return
    
def main():
    filename = input("Enter the locked zip file name "
                 "(Please include extension which is .zip"
                 "at the end of the file name): ")
    zfile=zipfile.ZipFile(filename)
    passfile= open('PasswordList.txt')
    for line in passfile.readlines():
        password = line.strip('\n')
        guess=extractfile(zfile,password)
        if guess:
            print('Your password = ' + password)
            break
        
if __name__=='__main__':
    main()