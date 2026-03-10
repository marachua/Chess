import tkinter as tk
from tkinter import PhotoImage
from controllers.game_controller import GameController
from models.board import Board
import os
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
        self.load_piece_images()
        self.create_board()
        self.draw_pieces()

        self.canvas_board.bind("<Motion>", self.on_mouse_move)
        self.canvas_board.bind("<Button-1>", self.on_cell_clicked)
    
    def create_board(self, active_coord: tuple = None):
        if active_coord:
            self.canvas_board.delete("cells")

        colors = ["#B3B3B3", "#3D3D3D"]
        active_colors = ["#92B895", "#37602F"]

        for row in range(8):
            for col in range(8):

                x0 = col * self.cell_size
                y0 = row * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size

                color_index = (row + col) % 2
                color = colors[color_index]

                if active_coord:
                    row_active, col_active = active_coord
                    if row == row_active and col == col_active:
                        color_index = (row + col) % 2
                        color = active_colors[color_index]


                self.canvas_board.create_rectangle(x0, y0, x1, y1, fill=color, outline="#3D3D3D", tags="cells")
        
    def load_piece_images(self):
        colors = ["white", "black"]
        piece_types = ["king", "queen", "rook", "bishop", "knight", "pawn"]

        current_file = os.path.abspath(__file__)
        current_dir = os.path.dirname(current_file)
        project_root = os.path.dirname(os.path.dirname(current_dir))
        image_gir = os.path.join(project_root, 'resources', 'pieces')

        for color in colors:
            for type_piece in piece_types:
                file_name = f"{color}_{type_piece}.png"
                filepath = os.path.join(image_gir, file_name)

                if not os.path.exists(filepath):
                    print("файл не найден - load_piece_images")
                    continue
        
                image_raw = Image.open(filepath)
                new_size = (int(self.cell_size), int(self.cell_size))
                image_res = image_raw.resize(new_size, Image.Resampling.LANCZOS)
                image = ImageTk.PhotoImage(image_res)

                key = f"{color}_{type_piece}"
                self.pieces_images[key]=image

    def draw_pieces(self):
        self.canvas_board.delete("piece") # удаление всех фигур с тегом piece
        for piece in self.board.get_pieces():
            row, col = piece.get_coords()
            x0 = col * self.cell_size + self.cell_size / 2
            y0 = row * self.cell_size + self.cell_size / 2
            x1 = x0 + self.cell_size
            y1 = y0 + self.cell_size
            fill_color = "white" if piece.get_color() == "white" else "black"

            image = self.pieces_images.get(f"{fill_color}_{piece.get_name()}")
            print(self.pieces_images)
            print(image)

            self.canvas_board.create_image(x0, y0, image=image, tag="piece")
            #self.canvas_board.create_oval(x0 ,y0, x1, y1, fill=fill_color, tags="piece")
    
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