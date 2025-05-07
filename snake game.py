import os
import time
import random

class Snake:
    def __init__(self, start_row, start_col):
        self.body = [[start_row, start_col], [start_row, start_col - 1], [start_row, start_col - 2]]
        self.direction = 'D' 

    def move(self):
        head = self.body[0][:]
        if self.direction == 'W':
            head[0] -= 1
        elif self.direction == 'S':
            head[0] += 1
        elif self.direction == 'A':
            head[1] -= 1
        elif self.direction == 'D':
            head[1] += 1
        self.body.insert(0, head)
        self.body.pop()

    def grow(self):
        tail = self.body[-1]
        self.body.append(tail[:]) 

    def set_direction(self, dir_input):
        opposite = {'W': 'S', 'S': 'W', 'A': 'D', 'D': 'A'}
        if dir_input.upper() in ['W', 'A', 'S', 'D'] and dir_input.upper() != opposite.get(self.direction):
            self.direction = dir_input.upper()

    def head(self):
        return self.body[0]

    def collision(self, rows, cols):
        head = self.head()
        return (
            head in self.body[1:] or
            head[0] == 0 or head[0] == rows - 1 or
            head[1] == 0 or head[1] == cols - 1
        )


class Food:
    def __init__(self, rows, cols, snake_body):
        self.rows = rows
        self.cols = cols
        self.position = []
        self.respawn(snake_body)

    def respawn(self, snake_body):
        while True:
            row = random.randint(1, self.rows - 2)
            col = random.randint(1, self.cols - 2)
            if [row, col] not in snake_body:
                self.position = [row, col]
                break


class Game:
    def __init__(self, rows=10, cols=20):
        self.rows = rows
        self.cols = cols
        self.snake = Snake(rows // 2, cols // 2)
        self.food = Food(rows, cols, self.snake.body)
        self.score = 0

    def draw(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for r in range(self.rows):
            row_str = ''
            for c in range(self.cols):
                if [r, c] == self.snake.head():
                    row_str += 'O'
                elif [r, c] in self.snake.body:
                    row_str += 'o'
                elif [r, c] == self.food.position:
                    row_str += '*'
                elif r == 0 or r == self.rows - 1 or c == 0 or c == self.cols - 1:
                    row_str += '#'
                else:
                    row_str += ' '
            print(row_str)
        print(f"Score: {self.score}")

    def play(self):
        while True:
            self.draw()
            direction = input("Move (W/A/S/D): ").upper()
            self.snake.set_direction(direction)
            self.snake.move()

            if self.snake.head() == self.food.position:
                self.snake.grow()
                self.score += 10
                self.food.respawn(self.snake.body)

            if self.snake.collision(self.rows, self.cols):
                self.draw()
                print("Game Over! Final Score:", self.score)
                break

            time.sleep(0.1)


if __name__ == "__main__":
    game = Game()
    game.play()
