from tkinter import *
import tkinter.font as tkf

def display():
    print(entUsername.get())
    lblFooter.config(text=entUsername.get()+" / "+entPassword.get())

root = Tk()
root.title('My first program')
root.iconbitmap('img.ico')
root.geometry('700x420')

lblCaption = Label(root, text='  LOGIN  ', bg='blue', fg='yellow', font=tkf.Font(family="Arial", size="20"))
lblCaption.grid(row=0, column=0, columnspan=3)

Label(root, text='').grid(row=1, column=1, columnspan=3)
Label(root, text='').grid(row=2, column=1, columnspan=3)
Label(root, text='').grid(row=3, column=1, columnspan=3)

lblUsername = Label(root, text='Username:', font=tkf.Font(family="Arial", size="15"))
lblUsername.grid(row=4, column=0, columnspan=1)

entUsername = Entry(root, font=tkf.Font(family="Arial", size="15"))
entUsername.grid(row=4, column=1, columnspan=2)


root.mainloop()
