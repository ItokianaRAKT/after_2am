from state import GameState
from game.day1 import day_one_start
from game.day2 import day_two_start
from game.day3 import day_three_start


def main():
    state = GameState()

    day_one_start(state)
    day_two_start(state)
    day_three_start(state)


if __name__ == "__main__":
    main()
