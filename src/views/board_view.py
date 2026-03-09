import tkinter as tk
from controllers.game_controller import GameController
from models.board import Board

import os
import cairosvg
from io import BytesIO
from PIL import Image, ImageTk


class ChessBoardGUI:
    def __init__(self, parent, controller: GameController, board: Board):
        self.board = board
        self.parent = parent
        self.controller = controller
        #for now key = sum(row + col): item = (pices_gui)
        self.pices_gui: dict = {}
        self.size_board = 500
        self.cell_size = self.size_board / 8
        self.canvas_board = tk.Canvas(parent, bg="#FFFFFF", width=self.size_board, height=self.size_board)
        self.canvas_board.pack()
        self.pieces_images = {}
        self.create_board()
        self.draw_pieces()
        self.load_piece_images()

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
        
    def load_piece_images(self):
        colors = ["white", "black"]
        piece_types = ["king", "queen", "rook", "bishop", "knight", "pawn"]

        current_file = os.path.abspath(__file__)
        current_dir = os.path.dirname(current_file)
        project_root = os.path.dirname(os.path.dirname(current_dir))
        image_gir = os.path.join(project_root, 'resources', 'pieces')

        for color in colors:
            for type_piece in piece_types:
                file_name = f"{color}_{type_piece}.svg"
                filepath = os.path.join(image_gir, file_name)

                if not os.path.exists(filepath):
                    print("файл не найден - load_piece_images")
                    continue

                out = BytesIO()
                cairosvg.svg2png(url=filepath, 
                                 write_to=out, 
                                 output_height=int(self.cell_size), 
                                 output_width=int(self.cell_size))
                out.seek(0)
                image = image.open(out)

                photo = ImageTk.PhotoImage(image)
                key = f"{color}_{type_piece}"

                self.pieces_images[key]=photo
        

        print("adada")
        print(self.pieces_images)

    def draw_pieces(self):
        self.canvas_board.delete("piece") # удаление всех фигур с тегом piece
        for piece in self.board.get_pieces():
            row, col = piece.get_coords()
            x0 = col * self.cell_size
            y0 = row * self.cell_size
            x1 = x0 + self.cell_size
            y1 = y0 + self.cell_size
            fill_color = "white" if piece.get_color() == "white" else "black"
            self.canvas_board.create_oval(x0 ,y0, x1, y1, fill=fill_color, tags="piece")
    
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