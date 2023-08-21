#label.py

# 3.1
import tkinter as tk

root = tk.Tk() #สร้าง window หลักของโปรแกรม
root.title("สนุกสนาน กับการเขียนโปรแกรม")
root.geometry("500x300+700+200") #WHXY

l1 = tk.Label(root, text="Hello Students!")#คำสั่ง Label()
l1.pack()

root.mainloop()

# 3.2
import tkinter as tk

root = tk.Tk() #สร้าง window หลักของโปรแกรม
root.title("สนุกสนาน กับการเขียนโปรแกรม")
root.geometry("500x300+700+200") #WHXY

l1 = tk.Label(root, text="Hello Students!")#คำสั่ง Label()
l1.pack()

l2 = tk.Label(root, text="สบาย ๆ")
l2.pack()

root.mainloop()

# 3.3
import tkinter as tk

root = tk.Tk() #สร้าง window หลักของโปรแกรม
root.title("สนุกสนาน กับการเขียนโปรแกรม")
root.geometry("500x300+700+200") #WHXY

l1 = tk.Label(root, text="เพื่อน 1\nเพื่อน 2\nเพื่อน 3\nเพื่อน 4\nเพื่อน 5")#คำสั่ง Label()
l1.pack()

root.mainloop()