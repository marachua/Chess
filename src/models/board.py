from models.piece import Piece, Pawn, Queen, King, Rook, Knight, Bishop

class Board:
    def __init__(self):
        #key = (row, col): item = piece
        self.pieces = {}
        self.setup_initial_position()

    def setup_initial_position(self):
        black_rook_first = Rook(0, 0, "black")
        self.pieces[black_rook_first.get_coords()] = black_rook_first
        black_rook_secont = Rook(0, 7, "black")
        self.pieces[black_rook_secont.get_coords()] = black_rook_secont 
        black_knight_first = Knight(0, 1, "black")
        self.pieces[black_knight_first.get_coords()] = black_knight_first
        black_knight_second = Knight(0, 6, "black")
        self.pieces[black_knight_second.get_coords()] = black_knight_second
        black_bishop_first = Bishop(0, 2, "black")
        self.pieces[black_bishop_first.get_coords()] = black_bishop_first
        black_bishop_secont = Bishop(0, 5, "black")
        self.pieces[black_bishop_secont.get_coords()] = black_bishop_secont
        black_king = King(0, 3, "black")
        self.pieces[black_king.get_coords()] = black_king
        black_queen = Queen(0, 4, "black")
        self.pieces[black_queen.get_coords()] = black_queen

        for i in range(0, 8):
            black_pawn = Pawn(1, i, "black")
            self.pieces[black_pawn.get_coords()] = black_pawn 
        
        white_rook_first = Rook(7, 0, "white")
        self.pieces[white_rook_first.get_coords()] = white_rook_first
        white_rook_secont = Rook(7, 7, "white")
        self.pieces[white_rook_secont.get_coords()] = white_rook_secont 
        white_knight_first = Knight(7, 1, "white")
        self.pieces[white_knight_first.get_coords()] = white_knight_first
        white_knight_second = Knight(7, 6, "white")
        self.pieces[white_knight_second.get_coords()] = white_knight_second
        white_bishop_first = Bishop(7, 2, "white")
        self.pieces[white_bishop_first.get_coords()] = white_bishop_first
        white_bishop_secont = Bishop(7, 5, "white")
        self.pieces[white_bishop_secont.get_coords()] = white_bishop_secont
        white_king = King(7, 3, "white")
        self.pieces[white_king.get_coords()] = white_king
        white_queen = Queen(7, 4, "white")
        self.pieces[white_queen.get_coords()] = white_queen

        for i in range(0, 8):
            white_pawn = Pawn(6, i, "white")
            self.pieces[white_pawn.get_coords()] = white_pawn 


    def get_pieces(self) -> list[Piece]:
        return self.pieces.values()

    def move_piece(self, from_pose: tuple, to_pose: tuple):
        piece: Piece = self.pieces.get(from_pose)
        if not piece:
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
    