#entry1.py

# 5.1
import tkinter as tk

root = tk.Tk()
title = "การใช้ Entry widget รับการกรอกข้อมูลของผู้ใช้"
root.title(title)
root.geometry('500x300+700+300')

e1 = tk.Entry(root) # คำสั่ง Entyr()
e1.pack()

root.mainloop()

# 5.2
import tkinter as tk

root = tk.Tk()
title = "การใช้ Entry widget รับการกรอกข้อมูลของผู้ใช้"
root.title(title)
root.geometry('500x300+700+300')

label = tk.Label(root, text="กรอกชื่อด้วยค่ะ : ")
label.pack()

e1 = tk.Entry(root) # คำสั่ง Entyr()
e1.pack()

root.mainloop()

# 5.3
import tkinter as tk

root = tk.Tk()
title = "การใช้ Entry widget รับการกรอกข้อมูลของผู้ใช้"
root.title(title)
root.geometry('500x300+700+300')

label = tk.Label(root, text="กรอกชื่อด้วยค่ะ : ")
label.pack()

e1 = tk.Entry(root) # คำสั่ง Entyr()
e1.pack()

b1 = tk.Button(root, text="คลิก")
b1.pack()

# root.mainloop()

# 5.4
import tkinter as tk

def greeting():
    message = "สวัสดีค่ะคุณ " + e1.get()
    label["text"] = message

root = tk.Tk()
title = "การใช้ Entry widget รับการกรอกข้อมูลของผู้ใช้"
root.title(title)
root.geometry('500x300+700+300')

label = tk.Label(root, text="กรอกชื่อด้วยค่ะ : ")
label.pack()

e1 = tk.Entry(root) # คำสั่ง Entyr()
e1.pack()

b1 = tk.Button(root, text="คลิก", command=greeting)
b1.pack()

root.mainloop()