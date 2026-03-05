import tkinter as tk
from controllers.game_controller import GameController

class ChessBoardGUI:
    def __init__(self, parent, controller: GameController, board):
        self.board = board
        self.parent = parent
        self.controller = controller
        self.size_board = 500
        self.cell_size = self.size_board / 8
        self.canvas_board = tk.Canvas(parent, bg="#FFFFFF", width=self.size_board, height=self.size_board)
        self.canvas_board.pack()
        self.create_board()

        self.canvas_board.bind("<Motion>", self.on_mouse_move)
        self.canvas_board.bind("<Button-1>", self.on_cell_clicked)
    
    def create_board(self):
        colors = ["#E5E2E2", "#5D5A5A"]

        for row in range(8):
            for col in range(8):
                x0 = col * self.cell_size
                y0 = row * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size

                color_index = (row + col) % 2
                color = colors[color_index]
                self.canvas_board.create_rectangle(x0, y0, x1, y1, fill=color, outline="#ABABAB")
            
    def draw_pieces(self):
        pieces = self.board.get_pieces()
        for piece in pieces:
            row, col = piece.get_coords()
            self.canvas_board.create_oval(row, col, row + self.cell_size, col + self.cell_size, fill=piece.get_color())

    def display_start_position_pieces(self):
        pass
    
    def on_mouse_move(self, event):
        row, col = self.get_cell_from_coords(event.x, event.y)
        if row is not None:
            self.controller.on_mouse_move(row, col)

    def on_cell_clicked(self, event):
        row, col = self.get_cell_from_coords(event.x, event.y)
        if row is not None:
            self.controller.on_cell_clicked(row, col)

    def get_cell_from_coords(self, x, y):
        if 0 <= x < self.size_board and 0 <= y < self.size_board:
            row = int(y // self.cell_size)
            col = int(x // self.cell_size)
            return row, col
        return None, None