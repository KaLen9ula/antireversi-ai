from reversi.reversi import Reversi
from reversi.controller import BotController, HumanController, prepare
from reversi.runner import Runner
from reversi.console_view import ConsoleView

game_info = prepare()
game = Reversi(game_info[2])
runner = Runner(game_info[0], game_info[1])
while not game.is_finished:
    runner.process(game)
