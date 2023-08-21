#second.py

# 2.1
import tkinter as tk

root = tk.Tk() #สร้าง window หลักของโปรแกรม
root.title("สนุกสนาน กับการเขียนโปรแกรม")

root.geometry("400x250") #กำหนดขนาด windows

root.mainloop()

# 2.2
import tkinter as tk

root = tk.Tk() #สร้าง window หลักของโปรแกรม
root.title("สนุกสนาน กับการเขียนโปรแกรม")

root.geometry("300x500") #กำหนดขนาด windows

root.mainloop()

# 2.3
import tkinter as tk

root = tk.Tk() #สร้าง window หลักของโปรแกรม
root.title("สนุกสนาน กับการเขียนโปรแกรม")

root.geometry("300x500") #กำหนดขนาด windows

root.mainloop()

# 2.4
import tkinter as tk

root = tk.Tk() #สร้าง window หลักของโปรแกรม
root.title("สนุกสนาน กับการเขียนโปรแกรม")

root.geometry("600x100") #กำหนดขนาด windows

root.mainloop()

# 2.4
import tkinter as tk

root = tk.Tk() #สร้าง window หลักของโปรแกรม
root.title("สนุกสนาน กับการเขียนโปรแกรม")

root.geometry("500x300+700+200") #กำหนดขนาด windows

root.mainloop()

# 2.5
import tkinter as tk

root = tk.Tk() #สร้าง window หลักของโปรแกรม
root.title("สนุกสนาน กับการเขียนโปรแกรม")

# Find Screen Size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Find Center Values
centerWidth = int(screen_width/3)
centerHeight = int(screen_height/4)

# Center Screen and change size to 500x500
root.geometry(f"500x500+{centerWidth}+{centerHeight}")

root.mainloop()

