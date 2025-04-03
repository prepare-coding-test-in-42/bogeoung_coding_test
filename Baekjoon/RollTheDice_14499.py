n, m, x, y = 0,0,0,0
def input_func():
    global n, m, x, y
    n, m, x, y, k = map(int , input().split())
    board = [[0 for _ in range(m)]for _ in range(n)]
    for i in range(n):
        board[i] = list(map(int, input().split()))

    command = list(map(int, input().split()))

    return board, command

def move(dice_list, move_index):
    if move_index == 1: # 동
        dice_list[0], dice_list[2], dice_list[3], dice_list[5] = dice_list[3], dice_list[0],dice_list[5],dice_list[2]
    if move_index == 2: # 서
        dice_list[0], dice_list[2], dice_list[3], dice_list[5] = dice_list[2], dice_list[5], dice_list[0], dice_list[3]
    if move_index == 3: # 북
        dice_list[0], dice_list[1], dice_list[4], dice_list[5] = dice_list[4], dice_list[0], dice_list[5], dice_list[1]
    if move_index == 4: # 남
        dice_list[0], dice_list[1], dice_list[4], dice_list[5] = dice_list[1], dice_list[5], dice_list[0], dice_list[4]

    return dice_list

def run(board, commands):
    TOP_INDEX = 0
    BOTTOM_INDEX = 5
    global n, m,x,y

    cur_x, cur_y = x,y
    dice_list = [0,0,0,0,0,0]
    move_direction = [[0,1], [0, -1], [-1, 0], [1,0]]
    for command in commands:
        new_x, new_y = cur_x + move_direction[command -1][0], cur_y + move_direction[command-1][1]
        if 0 <= new_x < n and 0 <= new_y < m:
            dice_list = move(dice_list, command)
            if board[new_x][new_y] == 0:
                board[new_x][new_y] = dice_list[BOTTOM_INDEX]
            elif board[new_x][new_y] != 0:
                dice_list[BOTTOM_INDEX] = board[new_x][new_y]
                board[new_x][new_y] = 0
            print(dice_list[TOP_INDEX])
            cur_x, cur_y = new_x, new_y


def main():
    board, commands = input_func()
    run(board, commands)

if __name__ == "__main__":
    main()
