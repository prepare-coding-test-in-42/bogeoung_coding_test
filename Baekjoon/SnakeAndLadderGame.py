from collections import deque

class Ladder:
    def __init__(self, s, e):
        self.start = s
        self.end = e


class Ladders:
    def __init__(self):
        self.ladders = []

    def add(self, ladder):
        self.ladders.append(ladder)

    def sort(self):
        self.ladders.sort(key=lambda x: -x.end)


class Snake:
    def __init__(self, s, e):
        self.start = s
        self.end = e


class Snakes:
    def __init__(self):
        self.snakes = []

    def add(self, snake):
        self.snakes.append(snake)

    def sort(self):
        self.snakes.sort(key=lambda x: -x.end)


LADDER_START, LADDER_END = 1, 2
SNAKE_START, SNAKE_END = 3, 4


def input_func():
    n, m = map(int, input().split())

    board = [[0, 0] for _ in range(100)]
    ladders = Ladders()
    for ladder_index in range(n):
        x, y = map(int, input().split())
        ladders.add(Ladder(x-1, y-1))
        board[x-1] = [1, ladder_index]
        # board[y-1] = [2, ladder_index]

    snakes = Snakes()
    for snake_index in range(m):
        x, y = map(int, input().split())
        snakes.add(Snake(x-1, y-1))
        board[x-1] = [3, snake_index]
        # board[y-1] = [4, snake_index]

    return ladders, snakes, board


def run(ladders, snakes, board):
    queue = deque()
    cur_move_times = 0
    queue.append([0, cur_move_times])
    visited = [False for _ in range(100)]
    while queue:
        cur_location, cur_move_times = queue.popleft()
        if cur_location >= 99:
            return cur_move_times

        for i in range(1, 7):
            new_location = cur_location + i
            if new_location >= 100:
                continue
            # 이동할 위치가 다리의 시작이라면
            if board[new_location][0] == 1:
                ladder_index = board[new_location][1]
                new_location = ladders.ladders[ladder_index].end
            # 이동할 위치가 뱀의 시작이라면
            elif board[new_location][0] == 3:
                snake_index = board[new_location][1]
                new_location = snakes.snakes[snake_index].end
            if visited[new_location]:
                continue
            visited[new_location] = True
            queue.append([new_location, cur_move_times + 1])
    return cur_move_times


def main():
    ladders, snakes, board = input_func()
    answer = run(ladders, snakes, board)
    print(answer)


if __name__ == "__main__":
    main()
