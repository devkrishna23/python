def notation_to_coor(position):
    file, rank = position[0].lower(), int(position[1])
    if file < 'a' or file > 'h' or rank < 1 or rank > 8:
        raise ValueError(f"Invalid chess square: {position}")
    return ((rank, ord(file.lower()) - 96))

def coor_to_notation(position):
    file, rank = position
    if file < 1 or file > 8 or rank < 1 or rank > 8:
        raise ValueError(f"Invalid coordinates: {position}")
    return f"{chr(rank + 96)}{file}"

def print_board(board):
    for row in range(8, 0, -1):
        line = []
        for col in range(1, 9):
            piece = board[(row, col)]
            if piece is None:
                line.append('.')
            else:
                line.append(str(piece))
        print(row, ' '.join(line))
    print("  a b c d e f g h")