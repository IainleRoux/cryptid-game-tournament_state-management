from sys import argv
from utils.file_reader import read_info_file, reset_game_info

# TODO: remove usage of info file completely (file_reader.py)

# TODO: Add game setup based on structure placement
def setup_board():
    read_info_file()


# TODO: Update board state based on move played (player, location, piece type)
def make_move(move: dict[str, str]):
    pass


def play_game():
    print("Starting the game...")
    reset_game_info()

    print("Game setup...")
    setup_board()

    while True:
        next_move = input('Enter next move: ')

        if next_move in ['exit', 'quit']:
            print("Exiting the game.")
            break

        make_move()


if __name__ == "__main__":
    cell_list, player_clues = read_info_file()

    if len(argv) > 1 and argv[1] in ['reset', 'setup']:
        reset_game_info()
        exit
    
    if len(argv) > 1 and argv[1] == 'play':
        play_game()
        exit
