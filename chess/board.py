from pieces import Pawn, Knight, Bishop, Rook, King, Queen
from board_setup import initial_board
from chess_utlis import notation_to_coor, coor_to_notation

class Board:
    def __init__(self):
        self.squares = initial_board()
    
    def print_board(self):
        for row in range(8, 0, -1):
            line = []
            for col in range(1, 9):
                piece = self.squares[(row, col)]
                if piece is None:
                    line.append('.')
                else:
                    line.append(str(piece))
            print(row, ' '.join(line))
        print("  a b c d e f g h")
    
    def move(self, from_sq, to_sq):
        from_sq = notation_to_coor(from_sq)
        piece = self.squares[from_sq]
        if piece is None:
            raise ValueError(f"No piece on {coor_to_notation(from_sq)}")
        to_sq = notation_to_coor(to_sq)
        captured = self.squares[to_sq]
        self.squares[to_sq] = piece
        self.squares[from_sq] = None 
        piece.position = to_sq
        return captured
    
    def legal_move(self, from_sq, to_sq):
        from_sq = notation_to_coor(from_sq)
        to_sq = notation_to_coor(to_sq)
        piece = self.squares[from_sq]
        if piece is None:
            return False
        moves = piece.possible_moves()
        return to_sq in moves
        # if isinstance(piece, Pawn):
        #     if piece.color == "white":
        #         return position