import tkinter as tk
from views.board_view import ChessBoardGUI
from controllers.game_controller import GameController
from models.board import Board
from PIL import Image, ImageTk
import cairosvg

class MainWindow:

    def __init__(self, controller: GameController):
        self.controller = controller
        self.root = tk.Tk()
        self.root.geometry("550x550")
        self.chess_board_gui = ChessBoardGUI(parent=self.root, controller=self.controller, board=self.controller.board)
        self.controller.view = self.chess_board_gui
    
    def run(self):
        self.root.mainloop()

class App:
    def __init__(self):
        #self.game =
        self.board = Board()
        self.game_controller = GameController(self.board)
        self.main_window = MainWindow(self.game_controller)
        
    def run(self):
        self.main_window.run()

if __name__ == "__main__":
    app = App()
    app.run()