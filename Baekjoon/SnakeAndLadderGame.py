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
        board[y-1] = [2, ladder_index]

    snakes = Snakes()
    for snake_index in range(m):
        x, y = map(int, input().split())
        snakes.add(Snake(x-1, y-1))
        board[x-1] = [3, snake_index]
        board[y-1] = [4, snake_index]

    # ladders.sort()
    snakes.sort()
    return ladders, snakes, board


def run(ladders, snakes, board):
    cur_position = 99
    dice_roll_count = 0
    while cur_position > 1:
        # print(f"cur_position : {cur_position}")
        candidate_ladders = []
        candidate_location = []
        for i in range(1, 7):
            # 탈 수 있는 다리가 6자리 내로 존재하는지 확인
            new_position = cur_position - i
            if new_position < 0:
                break
            if board[new_position][0] == LADDER_END:  # 다리의 도착지점이라면
                ladder_index = board[new_position][1]
                candidate_ladders.append(ladders.ladders[ladder_index])
                continue
            if board[new_position][0] in [2, 3]:  # 다리의 시작지점이거나 뱀의 시작, 도착지점이라면
                continue
            candidate_location.append(i)

        # 다리가 존재한다면, 가장 멀리 갈 수 있는 다리로 이동
        if candidate_ladders:
            candidate_ladders.sort(key=lambda x: x.start)
            cur_position = candidate_ladders[0].start
            # print(f"move with ladders")
        else:
            cur_position -= candidate_location[-1]
        # print(f"dice_updated")
        dice_roll_count += 1
    return dice_roll_count


def main():
    ladders, snakes, board = input_func()
    answer = run(ladders, snakes, board)
    print(answer)


if __name__ == "__main__":
    main()
