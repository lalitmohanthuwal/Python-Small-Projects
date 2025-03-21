from game import get_player_move
from game_board import GameBoard

def main():
    board = GameBoard()
    current_player = "X"
    
    print("Welcome to Tic Tac Toe!")
    print("Positions are numbered 0-8, left to right, top to bottom")
    
    while True:
        board.display()
        
        position = get_player_move(current_player)
        
        if not board.make_move(position, current_player):
            print("Invalid move, try again")
            continue
            
        if board.is_winner(current_player):
            board.display()
            print(f"Player {current_player} wins!")
            break
            
        if board.is_full():
            board.display()
            print("It's a tie!")
            break
            
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()