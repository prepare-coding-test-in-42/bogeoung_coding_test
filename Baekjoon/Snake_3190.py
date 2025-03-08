n = 0
def init_board():
    global n
    n = int(input())
    k = int(input())

    board = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(k):
        x,y = map(int,input().split())
        board[x-1][y-1] = 1

    l = int(input())
    l_list = []
    for i in range(l):
        l_list.append(list(input().split()))

    return board, l_list

def update_move_direction(cur_move_direction_index, char):
    if char == "D":
        cur_move_direction_index += 1
    elif char == "L":
        cur_move_direction_index -= 1
    if cur_move_direction_index >= 4:
        cur_move_direction_index -= 4
    elif cur_move_direction_index < 0:
        cur_move_direction_index += 4

    return cur_move_direction_index


def run(board, l_list):
    global n
    move_direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    cur_head_x , cur_head_y = 0, 0
    move_index = 0
    time = 0
    snake_queue = [[0,0]]
    while True:
        time += 1
        new_head_x, new_head_y = cur_head_x + move_direction[move_index][0], cur_head_y + move_direction[move_index][1]
        if new_head_x < 0 or new_head_x >= n or new_head_y < 0 or new_head_y >= n: # 머리가 벽에 닿는 경우
            return time
        if [new_head_x, new_head_y] in snake_queue: # 머리가 몸에 닿는 경우
            return time
        if board[new_head_x][new_head_y] == 1: # 사과가 존재한다면
            snake_queue.insert(0, [new_head_x, new_head_y])
            board[new_head_x][new_head_y] = 0
        else:
            snake_queue.insert(0, [new_head_x, new_head_y])
            snake_queue.pop()
        cur_head_x, cur_head_y = new_head_x, new_head_y
        if l_list and time == int(l_list[0][0]):
            move_index = update_move_direction(move_index, l_list[0][1])
            l_list.pop(0)


def main():
    board, l_list = init_board()
    print(run(board, l_list))


if __name__ == "__main__":
    main()
