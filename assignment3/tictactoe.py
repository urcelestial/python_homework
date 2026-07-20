class TictactoeException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class Board:

    valid_moves = [
        "upper left", "upper center", "upper right",
        "middle left", "center", "middle right",
        "lower left", "lower center", "lower right"
    ]

    def __init__(self):
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = "X"
        self.last_move = None

    def __str__(self):
        rows = ["|".join(row) for row in self.board_array]
        return "\n-----\n".join(rows) + "\n"
    
    def move(self, move_string):
        move_string = move_string.lower()

        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        
        move_mapping = {
            "upper left": (0, 0), "upper center": (0, 1), "upper right": (0, 2),
            "middle left": (1, 0), "center": (1, 1), "middle right": (1, 2),
            "lower left": (2, 0), "lower center": (2, 1), "lower right": (2, 2)
        }


        row, col = move_mapping[move_string]

        if self.board_array[row][col] != " ":
            raise TictactoeException("That spot is taken.")

        self.board_array[row][col] = self.turn
        self.last_move = move_string

        # Switch turns
        self.turn = "O" if self.turn == "X" else "X"

    def whats_next(self):
        lines = []
        
        # Add rows
        for row in self.board_array:
            lines.append(row)
            
        # Add columns
        for col_idx in range(3):
            lines.append([self.board_array[0][col_idx], self.board_array[1][col_idx], self.board_array[2][col_idx]])
            
        # Add diagonals
        lines.append([self.board_array[0][0], self.board_array[1][1], self.board_array[2][2]])
        lines.append([self.board_array[0][2], self.board_array[1][1], self.board_array[2][0]])

        for line in lines:
            if line == ["X", "X", "X"]:
                return (True, "X has won")
            if line == ["O", "O", "O"]:
                return (True, "O has won")

        # Check for tie
        board_full = True
        for row in self.board_array:
            if " " in row:
                board_full = False
                break
                
        if board_full:
            return (True, "Cat's Game")

        return (False, f"{self.turn}'s turn")



game_board = Board()

print("Welcome to Tic-Tac-Toe!")
print(game_board)

game_over = False

while not game_over:
    user_move = input(f"{game_board.turn}'s turn. Enter your move: ")
    
    try:
        game_board.move(user_move)
        print(game_board)
    except TictactoeException as error:
        print(f"\n❌ Error: {error.message}\n")
        continue

    game_over, status_message = game_board.whats_next()
    print(status_message)
    print("-" * 20)