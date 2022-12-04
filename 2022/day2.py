from enum import IntEnum

from puzzle_info import PuzzleInfo

WIN_PTS = 6
TIE_PTS = 3
LOSE_PTS = 0

class Moves(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

MOVE_MAP = {
    "A": Moves.ROCK,
    "B": Moves.PAPER,
    "C": Moves.SCISSORS,

    "X": Moves.ROCK,
    "Y": Moves.PAPER,
    "Z": Moves.SCISSORS,
}

OUTCOME_ADJUSTMENT = {
    "X": -1,
    "Y": 0,
    "Z": 1,
}


def get_throw_points(move_a, move_b):
    points_a = move_a
    points_b = move_b
    if move_a == move_b:
        points_a += TIE_PTS
        points_b += TIE_PTS
    elif (move_a == Moves.ROCK and move_b == Moves.SCISSORS) or move_a == move_b + 1:
        points_a += WIN_PTS
    else:
        points_b += WIN_PTS

    return points_a, points_b

def get_my_throw(move_a, outcome):
    move = move_a + OUTCOME_ADJUSTMENT[outcome]
    if move == 0:
        move = 3
    if move == 4:
        move = 1
    return Moves(move)


if __name__ == '__main__':
    info = PuzzleInfo()

    points = [0, 0]
    for line in info.input_lines:
        # Get moves as a tuple of Moves enums
        move_a, move_b = line.split()

        #Get this rounds score and add it to the running total

        # Pt.1
        #score = get_throw_points(MOVE_MAP[move_a], MOVE_MAP[move_b])

        # Pt.2
        move_a = MOVE_MAP[move_a]
        score = get_throw_points(move_a, get_my_throw(move_a, move_b))
        points = [sum(pts) for pts in zip(points, score)]

    print(points)
