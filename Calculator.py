import math
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import statistics
from sympy import Symbol, integrate, sympify
import sympy as sp
from scipy.stats import poisson
import scipy.stats as stats


#Scientific Calculator
def evaluate_expression(expr):
    try:
        expr = expr.replace("sin(", "math.sin(")
        expr = expr.replace("cos(", "math.cos(")
        expr = expr.replace("tan(", "math.tan(")
        expr = expr.replace("log(", "math.log10(")
        expr = expr.replace("ln(", "math.log(")
        expr = expr.replace("e(", "math.exp(")
        expr = expr.replace("π", str(math.pi))
        expr = expr.replace("abs(", "math.fabs(")
        expr = expr.replace("math.sqrt(", "math.sqrt(")
        return eval(expr)
    except Exception as e:
        return "Error"
    
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

    Button(root, text='√', command=lambda: button_click('math.sqrt(')).grid(row=3, column=0, sticky="nsew")
    Button(root, text='log10', command=lambda: button_click('log(')).grid(row=3, column=1, sticky="nsew")
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
    Button(root, text="=", command=calculate).grid(row=8, column=2, columnspan=2, sticky="nsew")
    Button(root, text="Back", command=Mainmenu).grid(row=8, column=4, columnspan=1, sticky="nsew")

#Graphic Calculator
def graphic_calculator():
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Graphic Calculator")

    def plot_graph():
        try:
            degree = int(degree_entry.get())
            coeffs = list(map(float, coeff_entry.get().split()))
            left = float(left_entry.get())
            right = float(right_entry.get())
            points = int(points_entry.get())

            if len(coeffs) != degree + 1:
                raise ValueError("Number of coefficients must match the degree + 1.")
            p = np.poly1d(coeffs)
            x = np.linspace(left, right, points)
            y = p(x)

            for widget in plot_frame.winfo_children():
                widget.destroy()

            fig, ax = plt.subplots(figsize=(5, 4))
            ax.plot(x, y)
            ax.set_title("Polynomial Graph")
            ax.set_xlabel("X-Axis")
            ax.set_ylabel("Y-Axis")
            ax.grid(True)

            canvas = FigureCanvasTkAgg(fig, master=plot_frame)
            canvas.get_tk_widget().pack()
            canvas.draw()

        except ValueError as e:
            error_label.config(text="Error: " + str(e))
    Button(root, text="Main Menu", command=Mainmenu).pack(pady=10)

    Label(root, text="Enter Degree of Polynomial:").pack()
    degree_entry = Entry(root)
    degree_entry.pack()

    Label(root, text="Enter Coefficients (space-separated):").pack()
    coeff_entry = Entry(root)
    coeff_entry.pack()

    Label(root, text="Enter Left Bound:").pack()
    left_entry = Entry(root)
    left_entry.pack()

    Label(root, text="Enter Right Bound:").pack()
    right_entry = Entry(root)
    right_entry.pack()

    Label(root, text="Enter Spacing Between Each Point:").pack()
    points_entry = Entry(root)
    points_entry.pack()

    Button(root, text="Plot Graph", command=plot_graph).pack(pady=10)

    error_label = Label(root, text="", fg="red")
    error_label.pack()

    plot_frame = Frame(root)
    plot_frame.pack()

#Statistics Calculator
def statistics_calculator():
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Statistics Calculator")

    def mean():
        numbers = list(map(float, number_entry.get().split()))
        mean = statistics.mean(numbers)
        result_label.config(text=f"Mean: {mean}")

    def median():
        numbers = list(map(float, number_entry.get().split()))
        median = statistics.median(numbers)
        result_label.config(text=f"Median: {median}")

    def mode():
        numbers = list(map(float, number_entry.get().split()))
        mode = statistics.mode(numbers)
        result_label.config(text=f"Mode: {mode}")
        
    def stdev():
        numbers = list(map(float, number_entry.get().split()))
        stdev = statistics.stdev(numbers)
        result_label.config(text=f"Standard Deviation: {stdev}")


    Button(root, text="Main Menu", command=Mainmenu).pack(pady=10)

    Label(root, text="Enter Numbers(space seperated):").pack()
    number_entry = Entry(root)
    number_entry.pack()

    Button(root, text="Mean", command=mean).pack(pady=10)

    Button(root, text="Median", command=median).pack(pady=10)

    Button(root, text="Mode", command=mode).pack(pady=10)

    Button(root, text="Standard Deviation", command=stdev).pack(pady=10)

    result_label = Label(root, text="", font=("Helvetica", 14))
    result_label.pack(pady=20)

#Calculus Calculator
def calculus_calculator():
    for widget in root.winfo_children():
        widget.destroy()
    root.title("Calculus Calculator")

    def integral():
        try:
            express=Calculus_entry.get()
            x = Symbol('x')
            f = sympify(express)
            result = integrate(f, x)
            result_label.config(text=f"Integral: {result}")
        except Exception as e:
            result_label.config(text=f"Error: {e}")

    def diffrentiate():
        try:
            express=Calculus_entry.get()
            x = sp.symbols('x')
            value = sp.parse_expr(express)
            derivative = sp.diff(value, x)
            result_label.config(text=f"Derivative: {derivative}")
        except Exception as e:
            result_label.config(text=f"Error: {e}")
    
    Button(root, text="Main Menu", command=Mainmenu).pack(pady=10)

    Label(root, text="Enter the expression to integrate (in terms of x): ").pack()
    Calculus_entry = Entry(root)
    Calculus_entry.pack()

    Button(root, text="Integrate", command=integral).pack(pady=10)

    Button(root, text="Diffrentiate", command=diffrentiate).pack(pady=10)

    result_label = Label(root, text="", font=("Helvetica", 14))
    result_label.pack(pady=20)

#Distributions
def Binomial_Distribution():
    for widget in root.winfo_children():
        widget.destroy()
    root.title("Binomial Distribution")
    def binomial():
        try:
            n = int(successes_entry.get())
            p = float(prob_entry.get())

            x = np.arange(0, n + 1)
            pmf = stats.binom.pmf(x, n, p)

            for widget in plot_frame.winfo_children():
                widget.destroy()

            fig, ax = plt.subplots(figsize=(5, 4))
            plt.bar(x, pmf)
            ax.set_title("Binomial Distribution (n={}, p={})".format(n, p))
            ax.set_xlabel("Number of Successes")
            ax.set_ylabel("Probability")
            ax.grid(False)

            canvas = FigureCanvasTkAgg(fig, master=plot_frame)
            canvas.get_tk_widget().pack()
            canvas.draw()
        except ValueError as e:
            error_label.config(text="Error: " + str(e))
    

    Button(root, text="Main Menu", command=Mainmenu).pack(pady=10)

    Label(root, text="Enter Number Of Successes:").pack()
    successes_entry = Entry(root)
    successes_entry.pack()

    Label(root, text="Enter Probability:").pack()
    prob_entry = Entry(root)
    prob_entry.pack()

    Button(root, text="Plot Graph", command=binomial).pack(pady=10)

    error_label = Label(root, text="", fg="red")
    error_label.pack()

    plot_frame = Frame(root)
    plot_frame.pack()


def Normal_Distribution():
    for widget in root.winfo_children():
        widget.destroy()
    root.title("Normal Distribution")

    def normal():
        try:
            mean = int(mean_entry.get())
            stdev = int(stdev_entry.get())
            size = int(size_entry.get())

            data = np.random.normal(mean, stdev, size)

            for widget in plot_frame.winfo_children():
                widget.destroy()

            fig, ax = plt.subplots(figsize=(5, 4))
            plt.hist(data, 100)
            plt.axvline(data.mean(), color = 'k', linestyle = 'dashed', linewidth = 2)
            ax.set_title("Normal Graph")
            ax.set_xlabel("X-Axis")
            ax.set_ylabel("Y-Axis")
            ax.grid(False)

            canvas = FigureCanvasTkAgg(fig, master=plot_frame)
            canvas.get_tk_widget().pack()
            canvas.draw()
        except ValueError as e:
            error_label.config(text="Error: " + str(e))
    

    Button(root, text="Main Menu", command=Mainmenu).pack(pady=10)

    Label(root, text="Enter Mean:").pack()
    mean_entry = Entry(root)
    mean_entry.pack()

    Label(root, text="Enter Standard Deviation:").pack()
    stdev_entry = Entry(root)
    stdev_entry.pack()

    Label(root, text="Enter Size Of Graph:").pack()
    size_entry = Entry(root)
    size_entry.pack()

    Button(root, text="Plot Graph", command=normal).pack(pady=10)

    error_label = Label(root, text="", fg="red")
    error_label.pack()

    plot_frame = Frame(root)
    plot_frame.pack()


def Poison_Distribution():
    for widget in root.winfo_children():
        widget.destroy()
    root.title("Poison Distribution")

    def poison():
        try:
            Lambda = int(Lambda_entry.get())
            Loc = int(loc_entry.get())
            left = float(Left_entry.get())
            right = float(Right_entry.get())

            array = np.arange(left, right, 0.5)
            graph = poisson.pmf(array, Lambda, Loc)
        

            for widget in plot_frame.winfo_children():
                widget.destroy()

            fig, ax = plt.subplots(figsize=(5, 4))
            ax.plot(array, graph)
            ax.set_title("Poisson Graph")
            ax.set_xlabel("X-Axis")
            ax.set_ylabel("Y-Axis")
            ax.grid(False)

            canvas = FigureCanvasTkAgg(fig, master=plot_frame)
            canvas.get_tk_widget().pack()
            canvas.draw()
        except ValueError as e:
            error_label.config(text="Error: " + str(e))
    

    Button(root, text="Main Menu", command=Mainmenu).pack(pady=10)

    Label(root, text="Enter Left Bound:").pack()
    Left_entry = Entry(root)
    Left_entry.pack()

    Label(root, text="Enter Right Bound:").pack()
    Right_entry = Entry(root)
    Right_entry.pack()

    Label(root, text="Enter Lambda:").pack()
    Lambda_entry = Entry(root)
    Lambda_entry.pack()

    Label(root, text="Enter Location:").pack()
    loc_entry = Entry(root)
    loc_entry.pack()

    Button(root, text="Plot Graph", command=poison).pack(pady=10)

    error_label = Label(root, text="", fg="red")
    error_label.pack()

    plot_frame = Frame(root)
    plot_frame.pack()



#Main Menu (function)
def Mainmenu():
    for widget in root.winfo_children():
        widget.destroy()
    root.title("Calculator Selector")

    menu = Menu(root)
    root.config(menu=menu)

    calc_menu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Calculator Type", menu=calc_menu)
    calc_menu.add_command(label="Scientific Calculator", command=scientific_calculator)
    calc_menu.add_command(label="Graphic Calculator", command=graphic_calculator)
    calc_menu.add_command(label="Statistics Calculator", command=statistics_calculator)
    calc_menu.add_command(label="Calculus Calculator", command=calculus_calculator)
    calc_menu.add_command(label="Binomial Graphing", command=Binomial_Distribution)
    calc_menu.add_command(label="Normal Graphing", command=Normal_Distribution)
    calc_menu.add_command(label="Poisson Graphing", command=Poison_Distribution)
    calc_menu.add_separator()
    calc_menu.add_command(label="Exit", command=root.quit)

    Label(root, text="Welcome to the Multi-Mode Calculator", font=("Helvetica", 16)).pack(pady=20)
    Label(root, text="Select a calculator type from the menu above.", font=("Helvetica", 12)).pack(pady=10)

#Starting the Main Menu
root = Tk()
root.title("Calculator Selector")

menu = Menu(root)
root.config(menu=menu)

calc_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Calculator Type", menu=calc_menu)
calc_menu.add_command(label="Scientific Calculator", command=scientific_calculator)
calc_menu.add_command(label="Graphic Calculator", command=graphic_calculator)
calc_menu.add_command(label="Statistics Calculator", command=statistics_calculator)
calc_menu.add_command(label="Calculus Calculator", command=calculus_calculator)
calc_menu.add_command(label="Binomial Graphing", command=Binomial_Distribution)
calc_menu.add_command(label="Normal Graphing", command=Normal_Distribution)
calc_menu.add_command(label="Poisson Graphing", command=Poison_Distribution)
calc_menu.add_separator()
calc_menu.add_command(label="Exit", command=root.quit)

Label(root, text="Welcome to the Multi-Mode Calculator", font=("Helvetica", 16)).pack(pady=20)
Label(root, text="Select a calculator type from the menu above.", font=("Helvetica", 12)).pack(pady=10)

root.mainloop()
