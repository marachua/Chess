from models.board import Board

class GameController():
    def __init__(self, board: Board):
        from views.board_view import ChessBoardGUI
        self.view: ChessBoardGUI = None
        
        self.board = board
        self.selected_pos = None
    
    def on_mouse_move(self, row, col):
        pass
        #print(f"движение мышки {row} {col}")
    
    def on_cell_clicked(self, row, col):
        if self.selected_pos is None:
            if self.board.is_on_cell_piece((row, col)): 
                self.selected_pos = (row, col)
                self.view.create_board((row, col))
                self.view.draw_pieces()
        else:
            success = self.board.move_piece(self.selected_pos, (row, col))
            if success:
                self.view.create_board()
                self.view.draw_pieces()
            self.selected_pos = None
            self.view.create_board()
            self.view.draw_pieces()
 


    
        
