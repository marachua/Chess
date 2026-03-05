from piece import Piece

class Board:
    def __init__(self):
        self.pieces = []
        example_piece = Piece(0, 0, "#855858")

    def get_pieces(self):
        return self.pieces