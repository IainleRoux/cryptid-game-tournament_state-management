from sys import argv
from utils.file_reader import read_info_file, reset_game_info

# TODO: remove usage of info file completely (file_reader.py)

# TODO: Add game setup based on structure placement
def setup_board():
    read_info_file()


# TODO: Update board state based on move played (player, location, piece type)
def make_move(move: dict[str, str]):
    pass
