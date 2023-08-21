#entry2.py
import tkinter as tk
def show_fullname():
    name = name_entry.get()
    surname = surname_entry.get()
    labelFullname["text"] = (name + ' ' + surname)

root = tk.Tk()
title = "การใช้ Entry widget รับการกรอกข้อมูลของผู้ใช้"
root.title(title)
root.geometry("500x300+700+300")

labelName = tk.Label(root, text="กรอกชื่อ")
labelName.pack()

name_entry = tk.Entry(root)
name_entry.pack()

labelSurname = tk.Label(root, text="กรอกนามสกุล")
labelSurname.pack()

surname_entry = tk.Entry(root)
surname_entry.pack()

labelFullname = tk.Label(root)
labelFullname.pack()

greet_button = tk.Button(root, text="คลิกดู ชื่อ-สกุล ของท่าน ", command= show_fullname)
greet_button.pack()

root.mainloop()



