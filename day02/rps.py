from enum import Enum


class Moves(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


WHAT_LOSES_TO = {Moves.ROCK: Moves.SCISSORS,
                 Moves.PAPER: Moves.ROCK,
                 Moves.SCISSORS: Moves.PAPER}
WHAT_WINS_AGAINST = {loser: winner for (winner, loser) in WHAT_LOSES_TO.items()}


def read_input(filename="input.txt"):
    with open(filename, "r") as file:
        for line in file:
            yield line[0], line[2]


def score_round(their_move, my_move):
    global WHAT_LOSES_TO
    if WHAT_LOSES_TO[their_move] == my_move:
        return 0 + my_move.value
    elif WHAT_LOSES_TO[my_move] == their_move:
        return 6 + my_move.value
    else:
        return 3 + my_move.value


def score_moves(moves):
    return sum(score_round(their_move, my_move) for (their_move, my_move) in moves)


def translate_move(move):
    return {"A": Moves.ROCK, "B": Moves.PAPER, "C": Moves.SCISSORS,
            "X": Moves.ROCK, "Y": Moves.PAPER, "Z": Moves.SCISSORS}[move]


def part1():
    moves = ((translate_move(their_move_but_encoded), translate_move(my_move_but_encoded))
             for (their_move_but_encoded, my_move_but_encoded)
             in read_input())
    print(score_moves(moves))


def pick_move(their_move, outcome):
    global WHAT_LOSES_TO
    global WHAT_WINS_AGAINST
    if outcome == "X":
        return WHAT_LOSES_TO[their_move]
    elif outcome == "Y":
        return their_move
    else:
        # Because of the cyclical structure of the game we could also use
        # WHAT_LOSES_TO[WHAT_LOSES_TO[their_move]] :)
        return WHAT_WINS_AGAINST[their_move]


def part2():
    decoded_input = ((translate_move[their_move_but_encoded], outcome)
                     for (their_move_but_encoded, outcome)
                     in read_input())
    moves = ((their_move, pick_move(their_move, outcome))
             for (their_move, outcome)
             in decoded_input)
    print(score_moves(moves))


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
