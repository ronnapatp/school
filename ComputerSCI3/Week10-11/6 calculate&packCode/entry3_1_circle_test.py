#entry3_1_circle_test.py
import tkinter as tk
def show_circle():
    radius = radius_entry.get()
    try:
        circleArea =
        circumference =
    except:
        circleArea = circumference = 'ข้อมูลผิดพลาด: กรุณากรอกข้อมูลเป็นตัวเลข'
    label_circleArea["text"] =
    label_circumference["text"] =

root = tk.Tk()
title = "การใช้ Entry widget คำนวณพื้นที่วงกลม และเส้นรอบวง"
root.title(title)
root.geometry("350x250+750+350")

label_radius = "กรอกรัศมี"
labelRadius = tk.Label(root, text=label_radius)
labelRadius.pack()

radius_entry = tk.Entry(root)
radius_entry.pack()

label_circleArea = tk.Label(root)
label_circleArea.pack()

label_circumference = tk.Label(root)
label_circumference.pack()

circle_button = tk.Button(root, text="คลิกเพื่อคำนวณ วงกลม", command= show_circle)
circle_button.pack()

root.mainloop()

