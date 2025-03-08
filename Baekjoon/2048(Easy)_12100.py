import copy

move_direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
max_value = 0
n = 0
def init_board():
    global n
    n = int(input())

    board = []
    for i in range(n):
        board.append(list(map(int, input().split())))
    return board

def update_max_value(board):
    global n
    global max_value
    max_num = 0
    for row in board:
        max_num = max(max_num, max(row))
    max_value = max(max_value, max_num)

def get_sum_direction(direction):
    if direction == [0, 1]: # 오른쪽으로 이동 -> 왼쪽방향으로 move를 수행
        return [[0, -1], "minus"]
    elif direction == [0, -1]:
        return [[0, 1], "plus"]
    elif direction == [1, 0]:
        return [[-1, 0], "minus"]
    elif direction == [-1, 0]:
        return [[1,0], "plus"]
def move_board(board, direction):
    global n
    new_board = copy.deepcopy(board)
    is_merged_board = [[False for _ in range(n)] for _ in range(n)]
    sum_direction, is_minus_plus = get_sum_direction(direction)
    if is_minus_plus == "minus":
        range_x = range(n-1, -1, -1)
    else:
        range_x = range(n)
    for i in range_x:
        for j in range_x:
            move(new_board, i, j, sum_direction, is_merged_board)

    for i in range_x:
        for j in range_x:
            move_without_merge(new_board, i, j, direction)

    return new_board

def move(board, row, col, direction, is_merged_board):
    global n
    cur_value = board[row][col]
    if cur_value == 0:
        return
    if is_merged_board[row][col] == True:
        return

    new_row, new_col = row + direction[0], col + direction[1]
    while n > new_row >= 0 and n > new_col >= 0:
        if board[new_row][new_col] == 0:
            board[new_row][new_col] = cur_value
            board[row][col] = 0
            row, col = new_row, new_col
            new_row += direction[0]
            new_col += direction[1]
        elif board[new_row][new_col] == cur_value:
            board[new_row][new_col] = cur_value * 2
            board[row][col] = 0
            is_merged_board[new_row][new_col] = True
            break
        else:
            break

def move_without_merge(board, row, col, direction):
    global n
    cur_value = board[row][col]
    if cur_value == 0:
        return

    new_row, new_col = row + direction[0], col + direction[1]
    while n > new_row >= 0 and n > new_col >= 0:
        if board[new_row][new_col] == 0:
            board[new_row][new_col] = cur_value
            board[row][col] = 0
            row, col = new_row, new_col
            new_row += direction[0]
            new_col += direction[1]
        else:
            break

def dfs(board, depth):
    if depth == 5:
        update_max_value(board)
        return
    for direction in move_direction:
        new_board = move_board(board, direction)
        # if new_board != board:
        dfs(new_board, depth + 1)


def main():
    board = init_board()
    dfs(board,0)
    print(max_value)

if __name__ == "__main__":
    main()