from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, row, col, color, name=None):
        self.name = name
        self.row = row
        self.col = col
        self.color = color
    
    def get_coords(self):
        return self.row, self.col

    def get_color(self):
        return self.color
    
    def set_coords(self, to_pose: tuple):
        self.row, self.col = to_pose
    
    @abstractmethod
    def get_possible_moves(self, board):
        pass

    def get_name(self):
        return self.name

class Pawn(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color, name="pawn")

    def get_possible_moves(self, board):
        return super().get_possible_move()

class Queen(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color, name="queen")

    def get_possible_moves(self, board):
        return super().get_possible_move()
    
class Bishop(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color, name="bishop")

    def get_possible_moves(self, board):
        return super().get_possible_move()
    
class Knight(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color, name="knight")

    def get_possible_moves(self, board):
        return super().get_possible_move()
    
class King(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color, name="king")

    def get_possible_moves(self, board):
        return super().get_possible_move()
    
class Rook(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color, name="rook")

    def get_possible_moves(self, board):
        return super().get_possible_move()