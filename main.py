import tkinter as tk
from tkinter import *

class App:
    def __init__(self):
        #self.controller =
        #self.game =
        #главное изначальное окно 
        self.main_window = MainWindow()

    def run(self):
        self.main_window.run()

class MainWindow:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x800")

        canvas = Canvas(self.root, bg="#FFFFFF", width=500, height=500)
        canvas.pack()

        canvas.create_rectangle(10, 10, 200, 200, fill="#E5A9A9")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()