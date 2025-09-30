from tkinter import *
root=Tk()
root.title("Number pad")
root.geometry("250x300")
#frame=Frame(master=root,height=200,width=360,bg="#d1b3f5")
nums=[[9,8,7],[6,5,4],[3,2,1],['#',0,'*']]
for i in range(4):
    root.rowconfigure(i,weight=1,minsize=50)
for i in range(3):
    root.columnconfigure(i,weight=1,minsize=75)
for i in range(4):
    for j in range(3):
        frame=Frame(
            master=root,
            relief=GROOVE,
            borderwidth=1
        )
        frame.grid(row=i,column=j)
        label=Label(master=frame,text=nums[i][j],bg="#e75f5f")
        label.pack(padx=3,pady=3)
root.mainloop()