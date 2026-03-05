class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
    
    def get_coords(self):
        return self.row, self.col

    def get_color(self):
        return self.color
    
    def set_coords(self, to_pose: tuple):
        self.row, self.col = to_pose