from models.piece import Piece

class Board:
    def __init__(self):
        #key = (row, col): item = piece
        self.pieces = {}
        example_piece_1 = Piece(0, 0, "white")
        example_piece_2 = Piece(5, 4, "black")

        self.pieces[(example_piece_1.row, example_piece_1.col)] = example_piece_1
        self.pieces[(example_piece_2.row, example_piece_2.col)] = example_piece_2

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
    