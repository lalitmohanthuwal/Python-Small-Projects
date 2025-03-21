from game_board import GameBoard

def get_player_move(current_player):
    while True:
        try:
            position = int(input(f"Player {current_player}, enter position (0-8): "))
            if 0 <= position <= 8:
                return position
            print("Please enter a number between 0 and 8")
        except ValueError:
            print("Please enter a valid number")