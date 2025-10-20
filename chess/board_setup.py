from pieces import Pawn, Knight, Bishop, Rook, King, Queen
from chess_utlis import notation_to_coor, coor_to_notation


def initial_board():
    board = {}
    order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

    for row in range(1, 9):
        for col in range(1, 9):
            position = coor_to_notation((row, col))
            if row == 1:
                piece_class =  order[col - 1]
                board[(row, col)] = piece_class("white", position)
            elif row == 2:
                board[(row, col)] = Pawn("white", position)
            elif row == 7:
                board[(row, col)] = Pawn("black", position)
            elif row == 8:
                piece_class =  order[col - 1]
                board[(row, col)] = piece_class("black", position)
            else:
                board[(row, col)] = None
    return board