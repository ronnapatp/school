#entry3.py
import tkinter as tk
def show_triangle_area():
    base = base_entry.get()
    height = height_entry.get()
    try:
        triangle = 1/2 * float(base) * float(height)
    except:
        triangle = 'ข้อมูลผิดพลาด: กรุณากรอกข้อมูลเป็นตัวเลข'
    label_triangle["text"] = str("{:.2f}".format(triangle))


root = tk.Tk()
title = "การใช้ Entry widget รับการกรอกข้อมูลของผู้ใช้ เพื่อคำนวณพื้นที่สามเหลี่ยม"
root.title(title)
root.geometry("500x300+700+300")

label_text_base = "กรอกความยาวฐาน"
labelbase = tk.Label(root, text=label_text_base)
labelbase.pack()

base_entry = tk.Entry(root)
base_entry.pack()

label_text_height = "กรอกความสูง"
labelheight = tk.Label(root, text=label_text_height)
labelheight.pack()

height_entry = tk.Entry(root)
height_entry.pack()

label_triangle = tk.Label(root)
label_triangle.pack()

greet_button = tk.Button(root, text="คลิกเพื่อคำนวณ พื้นที่สามเหลี่ยม ", command= show_triangle_area)
greet_button.pack()

root.mainloop()

