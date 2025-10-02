from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry('400x400')
root.title("Length converter app")
def msg():
    inches=float(name_var.get())
    cm=inches*2.54
    messagebox.showinfo('Conversion result',cm)
name_label=Label(root,text='enter value in inch')
name_var=StringVar()
name_entry=Entry(root,textvariable=name_var)
name_label.pack(pady=10)
name_entry.pack(pady=5)
button=Button(root,text="convert inches to cm",command=msg)
button.place(x=40,y=80)
def handle_keypress(event):
    print(event.char)
root.bind("<Key>",handle_keypress)
root.mainloop()
