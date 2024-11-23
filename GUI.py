from tkinter import *
import math
def evaluate_expression(expr):
    try:
        expr = expr.replace("sin(", "math.sin(")
        expr = expr.replace("cos(", "math.cos(")
        expr = expr.replace("tan(", "math.tan(")
        expr = expr.replace("log(", "math.log10(")
        expr = expr.replace("ln(", "math.log(")
        expr = expr.replace("e(", "math.exp(")
        expr = expr.replace("π", str(math.pi))
        expr = expr.replace("abs", "math.fabs")
        expr = expr.replace("**(1/", "math.pow(x, 1/y)")
        return eval(expr)
    except Exception as e:
        return "Error"

# Function to create the scientific calculator UI
def scientific_calculator():
    for widget in root.winfo_children():
        widget.destroy()  

    root.title("Scientific Calculator")
    global string, input
    string = ""
    input = StringVar()
    e = Entry(root, width=35, borderwidth=5, textvariable=input)
    e.grid(row=0, column=0, columnspan=5, padx=10)

    def button_click(symbol):
        global string
        string += str(symbol)
        input.set(string)

    def clear():
        global string
        string = ""
        input.set(string)

    def delete():
        global string
        string = string[:-1]
        input.set(string)

    def calculate():
        global string
        result = evaluate_expression(string)
        string = str(result)
        input.set(string)

    # Add Scientific Calculator Buttons
    Button(root, text="ABS", command=lambda: button_click("abs(")).grid(row=1, column=0, sticky="nsew")
    Button(root, text="MOD", command=lambda: button_click("%")).grid(row=1, column=1, sticky="nsew")
    Button(root, text="DIV", command=lambda: button_click("//")).grid(row=1, column=2, sticky="nsew")
    Button(root, text="x!", command=lambda: button_click("math.factorial(")).grid(row=1, column=3, sticky="nsew")
    Button(root, text='e', command=lambda: button_click(str(math.e))).grid(row=1, column=4, sticky="nsew")

    Button(root, text="sin", command=lambda: button_click("sin(")).grid(row=2, column=0, sticky="nsew")
    Button(root, text="cos", command=lambda: button_click("cos(")).grid(row=2, column=1, sticky="nsew")
    Button(root, text="tan", command=lambda: button_click("tan(")).grid(row=2, column=2, sticky="nsew")
    Button(root, text="π", command=lambda: button_click("π")).grid(row=2, column=3, sticky="nsew")
    Button(root, text='x^n', command=lambda: button_click('**')).grid(row=2, column=4, sticky="nsew")

    Button(root, text='\u221A', command=lambda: button_click('math.sqrt(')).grid(row=3, column=0, sticky="nsew")
    Button(root, text='log\u2081\u2080', command=lambda: button_click('log(')).grid(row=3, column=1, sticky="nsew")
    Button(root, text='ln', command=lambda: button_click('ln(')).grid(row=3, column=2, sticky="nsew")
    Button(root, text="e^x", command=lambda: button_click('math.exp(')).grid(row=3, column=3, sticky="nsew")
    Button(root, text="\u00B1", command=lambda: button_click('-')).grid(row=3, column=4, sticky="nsew")

    Button(root, text='(', command=lambda: button_click('(')).grid(row=4, column=0, sticky="nsew")
    Button(root, text=')', command=lambda: button_click(')')).grid(row=4, column=1, sticky="nsew")
    Button(root, text="csc", command=lambda: button_click("1/math.sin(")).grid(row=4, column=2, sticky="nsew")
    Button(root, text="sec", command=lambda: button_click("1/math.cos(")).grid(row=4, column=3, sticky="nsew")
    Button(root, text="cot", command=lambda: button_click("1/math.tan(")).grid(row=4, column=4, sticky="nsew")

    Button(root, text='7', command=lambda: button_click('7')).grid(row=5, column=0, sticky="nsew")
    Button(root, text="8", command=lambda: button_click('8')).grid(row=5, column=1, sticky="nsew")
    Button(root, text="9", command=lambda: button_click('9')).grid(row=5, column=2, sticky="nsew")
    Button(root, text='DEL', command=delete).grid(row=5, column=3, sticky="nsew")
    Button(root, text='CLR', command=clear).grid(row=5, column=4, sticky="nsew")

    Button(root, text='4', command=lambda: button_click('4')).grid(row=6, column=0, sticky="nsew")
    Button(root, text="5", command=lambda: button_click('5')).grid(row=6, column=1, sticky="nsew")
    Button(root, text="6", command=lambda: button_click('6')).grid(row=6, column=2, sticky="nsew")
    Button(root, text='*', command=lambda: button_click('*')).grid(row=6, column=3, sticky="nsew")
    Button(root, text='/', command=lambda: button_click('/')).grid(row=6, column=4, sticky="nsew")

    Button(root, text='1', command=lambda: button_click('1')).grid(row=7, column=0, sticky="nsew")
    Button(root, text="2", command=lambda: button_click('2')).grid(row=7, column=1, sticky="nsew")
    Button(root, text="3", command=lambda: button_click('3')).grid(row=7, column=2, sticky="nsew")
    Button(root, text='+', command=lambda: button_click('+')).grid(row=7, column=3, sticky="nsew")
    Button(root, text='-', command=lambda: button_click('-')).grid(row=7, column=4, sticky="nsew")

    Button(root, text='0', command=lambda: button_click('0')).grid(row=8, column=0, sticky="nsew")
    Button(root, text=".", command=lambda: button_click('.')).grid(row=8, column=1, sticky="nsew")
    Button(root, text="=", command=calculate).grid(row=8, column=2, columnspan=3, sticky="nsew")

def graphic_calculator():
    for widget in root.winfo_children():
        widget.destroy()  # Clear the window

    root.title("Graphic Calculator")
    Label(root, text="Graphic Calculator Coming Soon!", font=("Helvetica", 16)).pack(pady=20)

def statistics_calculator():
    for widget in root.winfo_children():
        widget.destroy()  # Clear the window

    root.title("Statistics Calculator")
    Label(root, text="Statistics Calculator Coming Soon!", font=("Helvetica", 16)).pack(pady=20)

# Main Root Window
root = Tk()
root.title("Calculator Selector")

# Main Menu
menu = Menu(root)
root.config(menu=menu)

calc_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Calculator Type", menu=calc_menu)
calc_menu.add_command(label="Scientific Calculator", command=scientific_calculator)
calc_menu.add_command(label="Graphic Calculator", command=graphic_calculator)
calc_menu.add_command(label="Statistics Calculator", command=statistics_calculator)
calc_menu.add_separator()
calc_menu.add_command(label="Exit", command=root.quit)

# Default View
Label(root, text="Welcome to the Multi-Mode Calculator", font=("Helvetica", 16)).pack(pady=20)
Label(root, text="Select a calculator type from the menu above.", font=("Helvetica", 12)).pack(pady=10)

root.mainloop()
