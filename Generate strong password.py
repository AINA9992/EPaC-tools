from tkinter import *
from random import randint 

root = Tk()
root.title('Codemy.com - Strong Password Generator')
# root.iconbitmap('C:\Users\hp\OneDrive - Universiti Sains Malaysia\Documents\GitHub\EPaC-tools\7')
# root.geometry("500X200")

my_password = chr(randint(33,126))

# generate random strong password
def new_rand():
    # clear entry box
    pw_entry.delete(0, END)

    # get PW length and convert to integer
    pw_length = int(my_entry.get())

    # create a variable to hold our password 
    my_password = ''

    # loop through password length 
    for x in range(pw_length):
        my_password += chr(randint(33,126))

    # output password to the screen
    pw_entry.insert(0, my_password)
 
 # copyy to clipboard
def clipper():
    # clear the clipboard
    root.clipboard_clear()

    #copy to clipboard
    root.clipboard_append(pw_entry.get())

# label frame
lf = LabelFrame(root, text="how many characters?")
lf.pack(pady=20)

# create entry box to designate Number of characters
my_entry = Entry(lf, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)

#create entry box for our returned password
pw_entry = Entry(root, text='', font=("Helvetica", 24), bd=0, bg="systembuttonface")
pw_entry.pack(pady=20)

# create a frame for our buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

# create our buttons
my_button = Button(my_frame, text="Generate Strong Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy to Clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)

root.mainloop()