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
lblCaption.pack()

Label(root,text='').pack()
Label(root,text='').pack()

lblUsername = Label(root, text='Username:', font=tkf.Font(family="Arial", size="15"))
lblUsername.pack()

entUsername = Entry(root, font=tkf.Font(family="Arial", size="15"))
entUsername.pack()

Label(root,text='').pack()
Label(root,text='').pack()

lblPassword = Label(root, text='Password:', font=tkf.Font(family="Arial", size="15"))
lblPassword.pack()

entPassword = Entry(root, font=tkf.Font(family="Arial", size="15"), show="*")
entPassword.pack()

Label(root,text='').pack()
Label(root,text='').pack()

btnClick = Button(root, text=" Click ", font=tkf.Font(family='Arial', size='15'), command=display)
btnClick.pack()

Label(root,text='').pack()
Label(root,text='').pack()
Label(root,text='').pack()
Label(root,text='').pack()

lblFooter = Label(root, text='')
lblFooter.pack()

root.mainloop()
