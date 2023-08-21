#entry1_4_geometry_pack.py
import tkinter as tk

root = tk.Tk()
title = "การใช้ Entry widget รับการกรอกข้อมูลของผู้ใช้"
root.title(title)
root.geometry('400x200+800+350')

label = tk.Label(root, text = "กรอกชื่อด้วยค่ะ : ")
label.pack(anchor=tk.NW, padx=10)
e1 = tk.Entry(root)
e1.pack(fill=tk.BOTH, expand = 0 , padx=10, pady=10) #expand True/False 1/0

b1 = tk.Button(root, text="คลิก")
b1.pack(anchor=tk.NE, padx=10)

root.mainloop()

