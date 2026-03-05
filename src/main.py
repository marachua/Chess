import tkinter as tk
from views.board_view import ChessBoardGUI
from controllers.game_controller import GameController
from models.board import Board

class MainWindow:

    def __init__(self, controller: GameController, board: Board):
        self.controller = controller
        self.board = board
        self.root = tk.Tk()
        self.root.geometry("550x550")
        self.chess_board_gui = ChessBoardGUI(parent=self.root, controller=self.controller, board=self.board)
    
    def run(self):
        self.root.mainloop()

class App:
    def __init__(self):
        self.game_controller = GameController()
        #self.game =
        self.board = Board()
        self.main_window = MainWindow(self.game_controller, self.board)
        
    def run(self):
        self.main_window.run()

if __name__ == "__main__":
    app = App()
    app.run()