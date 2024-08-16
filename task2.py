import tkinter as tk

# Function to update the expression in the text entry box
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

# Function to clear the text entry box
def clear():
    global expression
    expression = ""
    equation.set("")

# Driver code
if __name__ == "__main__":
    gui = tk.Tk()
    gui.configure(background="light blue") 
    gui.title("Simple Calculator")
    gui.geometry("400x400") 
    expression = ""
    equation = tk.StringVar()

    expression_field = tk.Entry(gui, textvariable=equation, font=('Arial', 18))
    expression_field.grid(columnspan=4, ipadx=70, ipady=10)

    button1 = tk.Button(gui, text=' 1 ', fg='black', bg='orange', command=lambda: press(1), height=2, width=10)
    button1.grid(row=2, column=0)

    button2 = tk.Button(gui, text=' 2 ', fg='black', bg='orange', command=lambda: press(2), height=2, width=10)
    button2.grid(row=2, column=1)

    button3 = tk.Button(gui, text=' 3 ', fg='black', bg='orange', command=lambda: press(3), height=2, width=10)
    button3.grid(row=2, column=2)

    button4 = tk.Button(gui, text=' 4 ', fg='black', bg='orange', command=lambda: press(4), height=2, width=10)
    button4.grid(row=3, column=0)

    button5 = tk.Button(gui, text=' 5 ', fg='black', bg='orange', command=lambda: press(5), height=2, width=10)
    button5.grid(row=3, column=1)

    button6 = tk.Button(gui, text=' 6 ', fg='black', bg='orange', command=lambda: press(6), height=2, width=10)
    button6.grid(row=3, column=2)

    button7 = tk.Button(gui, text=' 7 ', fg='black', bg='orange', command=lambda: press(7), height=2, width=10)
    button7.grid(row=4, column=0)

    button8 = tk.Button(gui, text=' 8 ', fg='black', bg='orange', command=lambda: press(8), height=2, width=10)
    button8.grid(row=4, column=1)

    button9 = tk.Button(gui, text=' 9 ', fg='black', bg='orange', command=lambda: press(9), height=2, width=10)
    button9.grid(row=4, column=2)

    button0 = tk.Button(gui, text=' 0 ', fg='black', bg='orange', command=lambda: press(0), height=2, width=10)
    button0.grid(row=5, column=0)

    plus = tk.Button(gui, text=' + ', fg='black', bg='orange', command=lambda: press("+"), height=2, width=10)
    plus.grid(row=2, column=3)

    minus = tk.Button(gui, text=' - ', fg='black', bg='orange', command=lambda: press("-"), height=2, width=10)
    minus.grid(row=3, column=3)

    multiply = tk.Button(gui, text=' * ', fg='black', bg='orange', command=lambda: press("*"), height=2, width=10)
    multiply.grid(row=4, column=3)

    divide = tk.Button(gui, text=' / ', fg='black', bg='orange', command=lambda: press("/"), height=2, width=10)
    divide.grid(row=5, column=3)

    equal = tk.Button(gui, text=' = ', fg='black', bg='orange', command=equalpress, height=2, width=10)
    equal.grid(row=5, column=2)

    clear = tk.Button(gui, text='Clear', fg='black', bg='orange', command=clear, height=2, width=10)
    clear.grid(row=5, column=1)

    gui.mainloop()
