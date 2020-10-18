import random

LETTERS = 'abcdefgh'
NUMBERS = '12345678'


def convert_to_index(inp):
    y = LETTERS.find(inp[0])
    x = NUMBERS.find(inp[1])
    return y, x


class HumanController():
    def get_input(self, game, color):
        coverage = game.get_coverage(color)
        while True:
            inp = input('> ')
            if inp.lower() == 'restart' or inp.lower() == 'finish':
                return inp.lower()
            if len(inp) < 3 and inp[0] in LETTERS and inp[1] in NUMBERS:
                cell_idx = convert_to_index(inp)
                if cell_idx in list(coverage.keys()):
                    return cell_idx
            print(f'Illegal command: {inp}')


class BotController():
    def get_input(self, game, color):
        coverage = game.get_coverage(color)
        return random.choice(list(coverage.keys()))


class AiController():
    pass


class TestController():
    pass


def prepare():
    player_one = None
    player_two = None
    black_hole = convert_to_index(input())
    ai_color = input()
    if ai_color == "black":
        player_one = AiController()
        player_two = TestController()
    else:
        player_one = TestController()
        player_two - AiController()

    return player_one, player_two, black_hole
