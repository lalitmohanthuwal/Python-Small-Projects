class GameBoard:
    def __init__(self):
        self.board = [" " for _ in range(9)]
    
    def make_move(self, position, player):
        if self.is_valid_move(position):
            self.board[position] = player
            return True
        return False
    
    def is_valid_move(self, position):
        return 0 <= position <= 8 and self.board[position] == " "
    
    def is_winner(self, player):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i:i+3] == [player] * 3:
                return True
        
        # Check columns
        for i in range(3):
            if self.board[i::3] == [player] * 3:
                return True
        
        # Check diagonals
        if self.board[0] == player and self.board[4] == player and self.board[8] == player:
            return True
        if self.board[2] == player and self.board[4] == player and self.board[6] == player:
            return True
        
        return False
    
    def is_full(self):
        return " " not in self.board
    
    def display(self):
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 6:
                print("-----------")