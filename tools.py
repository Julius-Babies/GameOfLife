def get_board_visual(board):
    out = ""
    for column in range(len(board[0])):
        for row in range(len(board)):
            if board[row][column] == 0:
                out = out + "🟥"
            else:
                out = out + "🟩"

        out = out + "\n"

    return out


def get_neighbours(board, x, y):
    neighbours = 0

    for row in range(3):
        for column in range(3):
            # ignore middle element (1|1)
            if not (row == 1 and column == 1):
                try:
                    neighbours = neighbours + get_board_element(board, x + row - 1, y + column - 1)
                except IndexError:
                    ...

    return neighbours


def get_board_element(board, row, column):
    try:
        return board[row][column]
    except IndexError:
        return 0


def clone_array(array):
    a = []
    for i in range(len(array)):
        a.append(array[i].copy())

    return a
