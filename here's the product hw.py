from tkinter import *
def show_product():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        product = num1 * num2
        result = "The product of the two numbers is: " + str(product)
    except ValueError:
        result = "Please enter valid numbers"
    text_box1.delete("1.0", END)
    text_box1.insert(END, result)
root = Tk()
root.title("Here's The Product (HW)")
root.geometry('600x500')
lbl = Label(text="Enter 2 numbers in each of the provided text boxes", fg="white", bg="#BF1559", height=2, width=300)
name_lbl = Label(text="After entering the numbers, the product will be displayed to you", fg="white", bg="#13A597")
entry1 = Entry()
entry2 = Entry()
greet_button = Button(text="Get the product", command=show_product)
text_box1 = Text(height=2)
lbl.pack()
name_lbl.pack()
entry1.pack()
entry2.pack()
greet_button.pack()
text_box1.pack()
root.mainloop()
