from tkinter import *
import tkinter.font as tkf

root = Tk()
root.title('My first program')
root.iconbitmap('img.ico')
root.geometry('700x350')

lblCaption = Label(root, text='  LOGIN  ', bg='blue', fg='yellow', font=tkf.Font(family="Arial", size="20"))
lblCaption.pack()

Label(root,text='').pack()
Label(root,text='').pack()

lblUsername = Label(root, text='Username:', font=tkf.Font(family="Arial", size="15"))
lblUsername.pack()

entUsername = Entry(root, font=tkf.Font(family="Arial", size="15"))
entUsername.pack()

root.mainloop()
