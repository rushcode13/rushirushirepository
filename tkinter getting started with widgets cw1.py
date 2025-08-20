from tkinter import  *
from datetime import date
root=Tk()
root.title("getting started with widgets")
root.geometry('400x300')
lbl=Label(text="hiiiii",fg="white",bg='#072F5F',height=1,width=300)
name_lbl=Label(text="sup peeps",fg="white",bg="#3895D3")
name_entry=Entry()
name=name_entry.get()
greet="hello,i hope you have a fine day,"+name
text_box=Text(height=3)
text_box.insert(END,date.today())
text_box.insert(END,greet)
lbl.pack()
name_lbl.pack()
name_entry.pack()
text_box.pack()
root.mainloop()