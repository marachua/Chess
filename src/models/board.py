from models.piece import Piece, Pawn, Queen, King

class Board:
    def __init__(self):
        #key = (row, col): item = piece
        self.pieces = {}
        black_pawn = Pawn(0, 0, "black", "pawn")
        white_queen = Queen(5, 4, "white", "queen")
        white_king = King(2, 4, "white", "king")

        self.pieces[(black_pawn.get_coords())] = black_pawn
        self.pieces[(white_king.get_coords())] = white_king
        self.pieces[(white_queen.get_coords())] = white_queen

    def get_pieces(self) -> list[Piece]:
        return self.pieces.values()
    
    def is_ligal_move(self, to_pose):
        # пока только проверка есть ли кто на клетке
        return self.is_on_cell_piece(to_pose)

    def move_piece(self, from_pose: tuple, to_pose: tuple):
        piece: Piece = self.pieces.get(from_pose)
        if not piece:
            return False
        
        if self.is_ligal_move(to_pose):
            return False

        del self.pieces[from_pose]
        row, col = to_pose
        self.pieces[to_pose] = piece
        piece.set_coords(to_pose)
        return True

    def is_on_cell_piece(self, coords: tuple):
        if self.pieces.get(coords):
            return True
        return False
    