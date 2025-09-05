from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
window=Tk()
window.tittle("Text editor")
window.geometry("600x500")
window.rowconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
def open_file():
    filepath=askopenfilename(
        filetypes=[("Text Files","*.txt"),("All Files","*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0,END)
    with open(filepath,"r") as input_file:
        text=input_file.read()
        txt_edit.insert(END,text)
        input_file.close()
    window.tittle(f"codindal's text editor-{filepath}")
txt_edit=Text(window)
fr_button=Frame(window,relief=RAISED,bd=2)
btn_open=Button(fr_button,text="open",command=open_file)
btn_open.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
fr_button.grid(row=0,column=0,sticky="ns")
txt_edit.grid(row=0,column=1,sticky="nsew")
window.mainloop()