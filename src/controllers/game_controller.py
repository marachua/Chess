from models.board import Board
from views.board_view import ChessBoardGUI

class GameController():
    def __init__(self, board: Board, view: ChessBoardGUI):
        self.board = board
        self.view = view
        self.selected_pos = None
    
    def on_mouse_move(self, row, col):
        print(f"движение мышки {row} {col}")
    
    def on_cell_clicked(self, row, col):
        if self.selected_pos is None:
            if self.board.is_on_cell_piece(row, col): 
                self.selected_pos = (row, col)
        else:
            success = self.board.move_piece(self.selected_pos, (row, col))
            if success:
                self.view.draw_pieces()
            self.selected_pos = None

    
        
