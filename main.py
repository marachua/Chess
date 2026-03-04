import tkinter as tk

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
        
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()