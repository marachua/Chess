from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, row, col, color, name):
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
    def get_possible_move(self):
        pass

    def get_name(self):
        return self.name


class Pawn(Piece):

    def get_possible_move(self):
        return super().get_possible_move()

class Queen(Piece):

    def get_possible_move(self):
        return super().get_possible_move()
    
class Bishop(Piece):

    def get_possible_move(self):
        return super().get_possible_move()
    
class Knight(Piece):

    def get_possible_move(self):
        return super().get_possible_move()
    
class King(Piece):

    def get_possible_move(self):
        return super().get_possible_move()
    
class Rook(Piece):

    def get_possible_move(self):
        return super().get_possible_move()