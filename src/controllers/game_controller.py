class GameController():
    def __init__(self):
        pass
    
    def on_mouse_move(self, row, col):
        print(f"движение мышки {row} {col}")
    
    def on_cell_clicked(self, row, col):
        print(f"нажатие по клетке {row} {col}")