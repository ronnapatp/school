#button.py

# 4.1
import tkinter as tk

root = tk.Tk() #สร้าง window หลักของโปรแกรม
root.title("สนุกสนาน กับการเขียนโปรแกรม")
root.geometry("500x300+700+200") #WHXY

b1 = tk.Button(root, text="คลิกที่นี่") #คำสั่ง Button()
b1.pack()

root.mainloop()

# 4.2.1
import tkinter as tk

root = tk.Tk() #สร้าง window หลักของโปรแกรม
root.title("สนุกสนาน กับการเขียนโปรแกรม")
root.geometry("500x300+700+200") #WHXY

b1 = tk.Button(root, text="คลิกที่นี่") #คำสั่ง Button()
b1.pack()

b2 = tk.Button(root, text="ออกจากโปรแกรม") #คำสั่ง Button()
b2.pack()

root.mainloop()

# 4.2.2
import tkinter as tk

root = tk.Tk() #สร้าง window หลักของโปรแกรม
root.title("สนุกสนาน กับการเขียนโปรแกรม")
root.geometry("500x300+700+200") #WHXY

b1 = tk.Button(root, text="คลิกที่นี่", width=25) #คำสั่ง Button()
b1.pack()

b2 = tk.Button(root, text="ออกจากโปรแกรม", width=25) #คำสั่ง Button()
b2.pack()

root.mainloop()

# 4.2.3
import tkinter as tk

root = tk.Tk() #สร้าง window หลักของโปรแกรม
root.title("สนุกสนาน กับการเขียนโปรแกรม")
root.geometry("500x300+700+200") #WHXY

b1 = tk.Button(root, text="คลิกที่นี่", width=25) #คำสั่ง Button()
b1.pack()

b2 = tk.Button(root, text="ออกจากโปรแกรม", width=25, command=root.destroy) #คำสั่ง Button()
b2.pack()

root.mainloop()