from tkinter import *
import zipfile
import hashlib

def extractfile(zfile,password):
    try:
        zfile.extractall(pwd=bytes(password, 'utf-8'))
        return password
    except:
        print('wrong password')
        return
    
def main():
    filename=input("Enter file name(please include extension which is .zip at the end of the file name): ")
    zfile=zipfile.ZipFile(filename)
    passfile= open('PasswordList.txt')
    for line in passfile.readlines():
        password = line.strip('\n')
        guess=extractfile(zfile,password)
        if guess:
            print('Password = ' + password)
            break
    
if __name__=='__main__':
    main()


