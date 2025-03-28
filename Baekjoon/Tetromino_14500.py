tetrominos = [[[0, 0], [0, 1], [0, 2], [0, 3]],
              [[0, 0], [0, 1], [1, 0], [1, 1]],
              [[0, 0], [1, 0], [2, 0], [2, 1]],
              [[0, 0], [1, 0], [2, 0], [2, -1]],
              [[0, 0], [1, 0], [1, 1], [2, 1]],
              [[0, 0], [1, 0], [1, -1], [2, -1]],
              [[0, 0], [0, 1], [0, 2], [1, 1]]]
n, m = 0, 0


def init_func():
    global n, m
    n, m = map(int, input().split())
    board = []

    for i in range(n):
        board.append(list(map(int, input().split())))
    return board


def roate_90(board):
    global n, m
    rotated_board = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            rotated_board[j][len(board) - 1 - i] = board[i][j]

    n, m = m, n
    return rotated_board


def is_valid_coordinate(tetromino_coordinate):
    global n, m
    for coor_x, coor_y in tetromino_coordinate:
        if 0 <= coor_x < n and 0 <= coor_y < m:
            continue
        else:
            return False
    return True


def get_sum_of_tetromino(tetromino_coordinate, board):
    sum = 0
    for coor_x, coor_y in tetromino_coordinate:
        sum += board[coor_x][coor_y]
    return sum


def count_max_num(board):
    global n, m
    max_sum_of_current_board = 0
    for i in range(n):
        for j in range(m):
            for tetromino in tetrominos:
                cur_tet = []
                for tet_x, tet_y in tetromino:
                    cur_tet.append([tet_x + i, tet_y + j])
                if is_valid_coordinate(cur_tet):
                    max_sum_of_current_board = max(get_sum_of_tetromino(cur_tet, board), max_sum_of_current_board)

    return max_sum_of_current_board


def run(board):
    answer = 0
    for i in range(4):  # 보드를 90도씩 회전
        answer = max(answer, count_max_num(board))
        board = roate_90(board)

    print(answer)


def main():
    board = init_func()
    run(board)


if __name__ == "__main__":
    main()
