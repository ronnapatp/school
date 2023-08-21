# Using Command Line

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
else:
    print("Invalid operation")

# Using Tkinter

import tkinter as tk

root = tk.Tk()

# Find Screen Size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Find Center Values
centerWidth = int(screen_width/3)
centerHeight = int(screen_height/4)

# Center Screen and change size to 500x500
root.geometry(f"500x500+{centerWidth}+{centerHeight}")


root.title("Calculator")

text = tk.Label(
    text = "CALCULATOR",
    background = "orange",
    foreground = "white",
    font=("Arial",20)
)


text.pack()

inputNum1 = tk.Entry(root)
inputNum1.pack()

inputNum2 = tk.Entry(root)
inputNum2.pack()


def output() :
    try:
        num1 = int(inputNum1.get())
        num2 = int(inputNum2.get())
    except ValueError:
        outPut.config(text="Your Data Must Be An Integer")
    else:
        result = num1 + num2
        outPut.config(text=f"Result is {result}")



outButton = tk.Button(text="Add",command=output)
outButton.pack()

outPut = tk.Label(text='')
outPut.pack()

root.mainloop()