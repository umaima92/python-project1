from tkinter import *
operator = ""
def btnclk(number):
    global operator
    operator += str(number)
    text_input.set(operator)
def btnclear():
    global operator
    operator = ""
    text_input.set(operator)

def btnequals():
    global operato
    equal = str(eval(operator))
    text_input.set(equal)

def square():
    global operator
    try:
        result = str(float(operator) ** 2)
        text_input.set(result)
        operator = result
    except Exception as e:
        text_input.set("Error")

def cube():
    global operator
    try:
        result = str(float(operator) ** 3)
        text_input.set(result)
        operator = result
    except Exception as e:
        text_input.set("Error")

def percentage():
    global operator
    try:
        result = str(float(operator) / 100)
        text_input.set(result)
        operator = result
    except Exception as e:
        text_input.set("Error")

def square_root():
    global operator
    try:
        result = str(float(operator) ** 0.5)
        text_input.set(result)
        operator = result
    except Exception as e:
        text_input.set("Error")



calc= Tk()
calc.title("GUI CALCULATOR")
text_input = StringVar()
display = Entry(calc, textvariable=text_input, bg='light blue', fg='black', font=('arial', 15, 'bold'),
                justify='right', bd=8)
display.grid(row=0, column=0, columnspan=5, pady=10)

#buttons
btn0 = Button(calc, text='0', font=('arial', 15, 'bold'), bd=8, padx=9, command=lambda: btnclk(0))
btn0.grid(row=4, column=1, padx=5, pady=5)
btn1 = Button(calc, text='1', font=('arial', 15, 'bold'), bd=8, padx=9, command=lambda: btnclk(1))
btn1.grid(row=3, column=0, padx=5, pady=5)
btn2 = Button(calc, text='2', font=('arial', 15, 'bold'), bd=8, padx=9, command=lambda: btnclk(2))
btn2.grid(row=3, column=1, padx=5, pady=5)
btn3 = Button(calc, text='3', font=('arial', 15, 'bold'), bd=8, padx=9, command=lambda: btnclk(3))
btn3.grid(row=3, column=2, padx=5, pady=5)
btn4 = Button(calc, text='4', font=('arial', 15, 'bold'), bd=8, padx=9, command=lambda: btnclk(4))
btn4.grid(row=2, column=0, padx=5, pady=5)
btn5 = Button(calc, text='5', font=('arial', 15, 'bold'), bd=8, padx=9, command=lambda: btnclk(5))
btn5.grid(row=2, column=1, padx=5, pady=5)
btn6 = Button(calc, text='6', font=('arial', 15, 'bold'), bd=8, padx=9, command=lambda: btnclk(6))
btn6.grid(row=2, column=2, padx=5, pady=5)
btn7 = Button(calc, text='7', font=('arial', 15, 'bold'), bd=8, padx=9, command=lambda: btnclk(7))
btn7.grid(row=1, column=0, padx=5, pady=5)
btn8 = Button(calc, text='8', font=('arial', 15, 'bold'), bd=8, padx=9, command=lambda: btnclk(8))
btn8.grid(row=1, column=1, padx=5, pady=5)
btn9 = Button(calc, text='9', font=('arial', 15, 'bold'), bd=8, padx=9, command=lambda: btnclk(9))
btn9.grid(row=1, column=2, padx=5, pady=5)

#calculator operations
Add = Button(calc, text='+', font=('arial', 15, 'bold'), bd=8, padx=9, command=lambda: btnclk("+"))
Add.grid(row=1, column=3, padx=5, pady=5)
Sub = Button(calc, text='-', font=('arial', 15, 'bold'), bd=8, padx=9, command=lambda: btnclk("-"))
Sub.grid(row=2, column=3, padx=5, pady=5)
mult = Button(calc, text='*', font=('arial', 15, 'bold'), bd=8, padx=9, command=lambda: btnclk("*"))
mult.grid(row=3, column=3, padx=5, pady=5)
div = Button(calc, text='/', font=('arial', 15, 'bold'), bd=8, padx=9, command=lambda: btnclk("/"))
div.grid(row=4, column=3, padx=5, pady=5)
square_btn = Button(calc, text='x^2', font=('arial', 15, 'bold'), bd=8, padx=9, command=square)
square_btn.grid(row=1, column=4, padx=5, pady=5)
cube_btn = Button(calc, text='x^3', font=('arial', 15, 'bold'), bd=8, padx=9, command=cube)
cube_btn.grid(row=2, column=4, padx=5, pady=5)
percentage_btn = Button(calc, text='%', font=('arial', 15, 'bold'), bd=8, padx=9, command=percentage)
percentage_btn.grid(row=3, column=4, padx=5, pady=5)
square_root_btn = Button(calc, text='sqrt', font=('arial', 15, 'bold'), bd=8, padx=9, command=square_root)
square_root_btn.grid(row=4, column=4, padx=5, pady=5)

#equal and clear
equal = Button(calc, text='=', font=('arial', 15, 'bold'), bd=8, padx=9, command=lambda: btnequals())
equal.grid(row=4, column=2, padx=5, pady=5)
clear = Button(calc, text='C', font=('arial', 15, 'bold'), bd=8, padx=9, command=lambda: btnclear())
clear.grid(row=4, column=0, padx=5, pady=5)




calc.mainloop()