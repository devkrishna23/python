from chess_utlis import notation_to_coor, coor_to_notation


class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = notation_to_coor(position)
    

    def get_notation(self):
        return coor_to_notation(self.position)
    
    def __str__(self):
        return self.symbol[self.color]
    
    def valid_offset(self, offset):
        row, col = self.position
        moves = []
        for dr, dc in offset:
            new_row, new_col = row + dr, col + dc
            if (1 <= new_row <= 8) and (1 <= new_col <= 8):
                moves.append((new_row, new_col))
        return moves
    
    def valid_direction(self, directions):
        row, col = self.position
        moves = []
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while (1 <= r <= 8) and (1 <= c <= 8):
                moves.append((r, c))
                r += dr
                c += dc
        return moves

class Pawn(Piece):
    symbol = {"white": "♙", "black": "♟"}
    def possible_moves(self):
        row, col = self.position
        moves = []
        if self.color == "white":
            direction = 1
            if row != 8:
                moves.append((row+direction, col))
                if row == 2:
                    moves.append((row+2*direction, col))
                if col != 8:
                    moves.append((row+direction, col+direction))
                if col != 1:
                    moves.append((row+direction, col-direction))
        else:
            direction = -1
            if row != 1:
                moves.append((row+direction, col))
                if row == 7:
                    moves.append((row+2*direction, col))
                if col != 8:
                    moves.append((row+direction, col+direction))
                if col != 1:
                    moves.append((row+direction, col-direction))
        return moves

class Rook(Piece):
    symbol = {"white": "♖", "black": "♜"}
    def possible_moves(self):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        return self.valid_direction(directions)

class Knight(Piece):
    symbol = {"white": "♘", "black": "♞"}
    def possible_moves(self):
        offsets = [(+2, +1), (+1, +2), (-2, +1), (-1, +2), (-1, -2), (-2, -1), (+2, -1), (+1, -2)]
        return self.valid_offset(offsets)

class Bishop(Piece):
    symbol = {"white": "♗", "black": "♝"}
    def possible_moves(self):
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)] 
        return self.valid_direction(directions)

class Queen(Piece):
    symbol = {"white": "♕", "black": "♛"}
    def possible_moves(self):
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]
        return self.valid_direction(directions)

class King(Piece):
    symbol = {"white": "♔", "black": "♚"}
    def possible_moves(self):
        offsets = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]
        return self.valid_offset(offsets)