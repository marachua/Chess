import tkinter as tk
from board import ChessBoardGUI
from gameController import GameController

class MainWindow:

    def __init__(self, controller: GameController):
        self.controller = controller
        self.root = tk.Tk()
        self.root.geometry("800x800")
        self.chess_board_gui = ChessBoardGUI(parent=self.root, controller=self.controller)
    
    def run(self):
        self.root.mainloop()

class App:
    def __init__(self):
        self.game_controller = GameController()
        #self.game =
        self.main_window = MainWindow(self.game_controller)

    def run(self):
        self.main_window.run()

if __name__ == "__main__":
    app = App()
    app.run()