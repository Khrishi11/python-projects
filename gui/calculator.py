from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Global variables to store the first number and the operation type
operation = ""
f_num = None

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    global f_num
    global operation
    first_number = e.get()
    operation = 'addition'
    f_num = float(first_number)
    e.insert(END, "+")  # Add the operator to the display

def button_equal():
    expression = e.get()
    try:
        result = eval(expression)
        e.delete(0, END)
        e.insert(0, result)
    except Exception as ex:
        e.delete(0, END)
        e.insert(0, "Error")

def button_subtract():
    global f_num
    global operation
    first_number = e.get()
    operation = 'subtraction'
    f_num = float(first_number)
    e.insert(END, "-")  # Add the operator to the display

def button_multiply():
    global f_num
    global operation
    first_number = e.get()
    operation = 'multiplication'
    f_num = float(first_number)
    e.insert(END, "*")  # Add the operator to the display

def button_divide():
    global f_num
    global operation
    first_number = e.get()
    operation = 'division'
    f_num = float(first_number)
    e.insert(END, "/")  # Add the operator to the display

# Define buttons
b1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
b2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
b3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
b4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
b5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
b6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
b7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
b8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
b9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
b0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

b_add = Button(root, text="+", padx=39, pady=20, command=button_add)
b_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
b_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)

b_subtract = Button(root, text="-", padx=41, pady=20, command=button_subtract)
b_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
b_divide = Button(root, text="/", padx=41, pady=20, command=button_divide)

# Put the buttons on the screen
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

b0.grid(row=4, column=0)

b_add.grid(row=5, column=0)
b_clear.grid(row=4, column=1, columnspan=2)
b_equal.grid(row=5, column=1, columnspan=2)

b_subtract.grid(row=6, column=0)
b_multiply.grid(row=6, column=1)
b_divide.grid(row=6, column=2)

root.mainloop()
