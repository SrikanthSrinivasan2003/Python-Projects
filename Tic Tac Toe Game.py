class Board:
    def __init__(self):
        self.grid = [' ' for _ in range(9)]

    def display(self):
        for i in range(3):
            row = self.grid[i*3:(i+1)*3]
            print(f" {row[0]} | {row[1]} | {row[2]} ")
            if i < 2:
                print("---+---+---")

    def update(self, position, symbol):
        if self.grid[position] == ' ':
            self.grid[position] = symbol
            return True
        return False

    def is_full(self):
        return ' ' not in self.grid

    def check_winner(self, symbol):
        wins = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        return any(all(self.grid[i] == symbol for i in line) for line in wins)


class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = 'X'

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        self.board.display()
        while True:
            try:
                move = int(input(f"Player {self.current_player}, choose position (1-9): ")) - 1
                if move < 0 or move >= 9:
                    print("Invalid input.")
                    continue
                if not self.board.update(move, self.current_player):
                    print("Position already taken.")
                    continue
            except ValueError:
                print("Enter a valid number.")
                continue

            self.board.display()

            if self.board.check_winner(self.current_player):
                print(f"Player {self.current_player} wins!")
                break
            if self.board.is_full():
                print("It's a draw!")
                break

            self.switch_player()


if __name__ == "__main__":
    game = Game()
    game.play()
