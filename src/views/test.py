from tkinter import *
import os
from PIL import Image, ImageTk
 
root = Tk()
root.title("METANIT.COM")
root.geometry("300x250")
 
canvas = Canvas(bg="white", width=2000, height=2000)
canvas.pack()

path = "C:/Users/kokosiiik/Desktop/projects/Chess/src/views/black_queen.png"
image = Image.open(path)
new_size = (100, 100)
image_res = image.resize(new_size, Image.Resampling.LANCZOS)
tk_image = ImageTk.PhotoImage(image_res)

canvas.create_image(0, 0, anchor=NW, image=tk_image)
 
root.mainloop()