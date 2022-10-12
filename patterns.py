import random


def generate_empty_board(width, height):
    board = list()
    for x in range(width):
        columns = list()
        for y in range(height):
            columns.append(0)

        board.append(columns)

    return board


def generate_board(width, height):
    field = list()
    for row in range(width):
        row = list()
        for column in range(height):
            row.append(int(random.randint(0, 10) == 0))

        field.append(row)

    return field


def generate_pattern_board(width, height, pattern):
    offset_x = round(width / 2) - round(len(pattern[0]) / 2)
    offset_y = round(height / 2) - round(len(pattern) / 2)

    board = generate_empty_board(width, height)
    for row in range(len(pattern)):
        for column in range(len(pattern[0])):
            board[offset_x + row][offset_y + column] = pattern[row][column]

    return board


def generate_block(width, height):
    pattern = [[1, 1], [1, 1]]
    return generate_pattern_board(width, height, pattern)


def generate_beehive(width, height):
    pattern = [
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [0, 1, 1, 0]
    ]

    return generate_pattern_board(width, height, pattern)


def generate_blinker(width, height):
    pattern = [
        [1],
        [1],
        [1]
    ]
    return generate_pattern_board(width, height, pattern)


def generate_clock(width, height):
    pattern = [
        [0, 1, 0, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 0, 1, 0]
    ]
    return generate_pattern_board(width, height, pattern)


def generate_turtle(width, height):
    pattern = [
        [0, 1, 0, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 0, 1, 0]
    ]
    return generate_pattern_board(width, height, pattern)


def generate_bipole(width, height):
    pattern = [
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1],
    ]
    return generate_pattern_board(width, height, pattern)


def generate_tripole(width, height):
    pattern = [
        [1, 1, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 1, 1]
    ]
    return generate_pattern_board(width, height, pattern)


def generate_pulsator(width, height):
    pattern = [
        [0, 1, 0],
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0],
        [0, 1, 0]
    ]
    return generate_pattern_board(width, height, pattern)


def generate_tuemmler(width, height):
    pattern = [
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 1, 1, 0]
    ]

    return generate_pattern_board(width, height, pattern)


def generate_octagon(width, height):
    pattern = [
        [0, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 1],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 1],
        [0, 1, 0, 0, 1, 0]
    ]

    return generate_pattern_board(width, height, pattern)


def generate_spaceship1(width, height):
    pattern = [
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 1, 0, 0, 1],
        [0, 0, 1, 1, 1]
    ]

    return generate_pattern_board(width, height, pattern)
