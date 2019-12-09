import tkinter as tk
from tkinter import *


root = tk.Tk()
root.title("Calculator")
root.geometry("361x520")
root.resizable(0, 0)

tot_font = ("Helvetica", "26")
but_font = ("Times", "20", "bold")
expression = ""


def backspace():
    # Function to remove the last character added
    global expression
    expression = expression[0:len(expression) - 1]
    equation.set(expression)


def number(num):
    # function for typing expression
    global expression
    expression = expression + str(num)
    equation.set(expression)


def clr():
    # function to clear the expression
    global expression
    expression = ""
    equation.set(expression)


def end():
    # function to evaluate the expression and give an answer
    global expression
    total = str(eval(expression))
    equation.set(total)
    expression = ""


# Text that goes into evaluation box needs to be StringVar
equation = StringVar()

# Evaluation box where string gets evaluated
eval_box = tk.Entry(root, textvariable=equation, bd="4", relief="ridge", width="14", font=tot_font, bg="#fafafa")
eval_box.grid(row=0, column=0, ipady="20", ipadx="4", columnspan="100", sticky="nsew")

# Buttons used to change expression in evaluation box
clr_button = tk.Button(root, text="Clear", font=but_font, bg="#efefef", justify="center", bd="2", height="2",
                       cursor="hand2", width="5", relief="ridge", command=lambda: clr())
clr_button.grid(row=1, column=0)
div_button = tk.Button(root, text="÷", font=but_font, bg="#efefef", justify="center", bd="2", height="2",
                       cursor="hand2", width="5", relief="ridge", command=lambda: number("/"))
div_button.grid(row=1, column=1)
mult_button = tk.Button(root, text="X", font=but_font, bg="#efefef", justify="center", bd="2", height="2",
                        cursor="hand2", width="5", relief="ridge", command=lambda: number("*"))
mult_button.grid(row=1, column=2)
bck_button = tk.Button(root, text="←", font=but_font, bg="#efefef", justify="center", bd="2", height="2",
                       cursor="hand2", width="5", relief="ridge", command=lambda: backspace())
bck_button.grid(row=1, column=3)
but7 = tk.Button(root, text="7", font=but_font, bg="#efefef", justify="center", bd="2", height="2", cursor="hand2",
                 width="5", relief="ridge", command=lambda: number(7))
but7.grid(row=2, column=0)
but8 = tk.Button(root, text="8", font=but_font, bg="#efefef", justify="center", bd="2", height="2", cursor="hand2",
                 width="5", relief="ridge", command=lambda: number(8))
but8.grid(row=2, column=1)
but9 = tk.Button(root, text="9", font=but_font, bg="#efefef", justify="center", bd="2", height="2", cursor="hand2",
                 width="5", relief="ridge", command=lambda: number(9))
but9.grid(row=2, column=2)
plus_but = tk.Button(root, text="+", font=but_font, bg="#efefef", justify="center", bd="2", height="2", cursor="hand2",
                     width="5", relief="ridge", command=lambda: number("+"))
plus_but.grid(row=2, column=3)
but4 = tk.Button(root, text="4", font=but_font, bg="#efefef", justify="center", bd="2", height="2", cursor="hand2",
                 width="5", relief="ridge", command=lambda: number(4))
but4.grid(row=3, column=0)
but5 = tk.Button(root, text="5", font=but_font, bg="#efefef", justify="center", bd="2", height="2", cursor="hand2",
                 width="5", relief="ridge", command=lambda: number(5))
but5.grid(row=3, column=1)
but6 = tk.Button(root, text="6", font=but_font, bg="#efefef", justify="center", bd="2", height="2", cursor="hand2",
                 width="5", relief="ridge", command=lambda: number(6))
but6.grid(row=3, column=2)
min_but = tk.Button(root, text="-", font=but_font, bg="#efefef", justify="center", bd="2", height="2", cursor="hand2",
                    width="5", relief="ridge", command=lambda: number("-"))
min_but.grid(row=3, column=3)
but1 = tk.Button(root, text="1", font=but_font, bg="#efefef", justify="center", bd="2", height="2", cursor="hand2",
                 width="5", relief="ridge", command=lambda: number(1))
but1.grid(row=4, column=0)
but2 = tk.Button(root, text="2", font=but_font, bg="#efefef", justify="center", bd="2", height="2", cursor="hand2",
                 width="5", relief="ridge", command=lambda: number(2))
but2.grid(row=4, column=1)
but3 = tk.Button(root, text="3", font=but_font, bg="#efefef", justify="center", bd="2", height="2", cursor="hand2",
                 width="5", relief="ridge", command=lambda: number(3))
but3.grid(row=4, column=2)
equal_but = tk.Button(root, text="=", font=but_font, bg="#efefef", justify="center", bd="2", height="5", cursor="hand2",
                      width="5", relief="ridge", command=lambda: end())
equal_but.grid(row=4, column=3, rowspan=3)
but_pers = tk.Button(root, text="Power", font=but_font, bg="#efefef", justify="center", bd="2", height="2",
                     cursor="hand2", width="5", relief="ridge", command=lambda: number("**"))
but_pers.grid(row=5, column=0)
but0 = tk.Button(root, text="0", font=but_font, bg="#efefef", justify="center", bd="2", height="2", cursor="hand2",
                 width="5", relief="ridge", command=lambda: number(0))
but0.grid(row=5, column=1)
but_point = tk.Button(root, text=".", font=but_font, bg="#efefef", justify="center", bd="2", height="2", cursor="hand2",
                      width="5", relief="ridge", command=lambda: number("."))
but_point.grid(row=5, column=2)

root.mainloop()
