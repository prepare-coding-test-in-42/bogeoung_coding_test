from collections import deque

EMPTY_SPACE = "."
WALL = "#"
HOLE = "O"
BLUE_BEAD = "B"
RED_BEAD = "R"
n, m = 0, 0
move_direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def input_func():
    n, m = map(int, input().split())
    input_arr = []

    for i in range(n):
        input_arr.append(list(input()))
    return n, m, input_arr

def find_color_bead(input_arr):
    r_loc, b_loc = [], []
    for row in range(len(input_arr)):
        for col in range(len(input_arr[row])):
            if input_arr[row][col] == RED_BEAD:
                r_loc = [row, col]
            elif input_arr[row][col] == BLUE_BEAD:
                b_loc = [row, col]

    return r_loc, b_loc

def move(x, y, direction, input_arr):
    cnt = 0
    dx = direction[0]
    dy = direction[1]
    while input_arr[x+dx][y+dy] != WALL and input_arr[x][y] != HOLE:
        x, y = x + dx, y + dy
        cnt += 1

    return x, y, cnt
def run(r_loc, b_loc, input_arr):
    visited  = []
    queue = deque()
    r_cur_x, r_cur_y = r_loc
    b_cur_x, b_cur_y = b_loc
    queue.append((r_cur_x, r_cur_y, b_cur_x, b_cur_y, 1))

    while queue:
        r_cur_x, r_cur_y, b_cur_x, b_cur_y, count = queue.popleft()

        if count > 10:
            break

        for direction in move_direction:
            r_new_x, r_new_y, r_cnt = move(r_cur_x, r_cur_y, direction, input_arr)
            b_new_x, b_new_y, b_cnt = move(b_cur_x, b_cur_y, direction, input_arr)

            if input_arr[b_new_x][b_new_y] == HOLE:
                continue

            if input_arr[r_new_x][r_new_y] == HOLE:
                print(count)
                return

            if r_new_x == b_new_x and r_new_y == b_new_y:
                if r_cnt > b_cnt:
                    r_new_x -= direction[0]
                    r_new_y -= direction[1]
                else:
                    b_new_x -= direction[0]
                    b_new_y -= direction[1]

            if (r_new_x, r_new_y, b_new_x, b_new_y) not in visited:
                visited.append((r_new_x, r_new_y, b_new_x, b_new_y))
                queue.append((r_new_x, r_new_y, b_new_x, b_new_y, count + 1))

    print(-1)



def main():
    n, m, input_arr = input_func()
    r_loc, b_loc = find_color_bead(input_arr)
    run(r_loc, b_loc, input_arr)


if __name__ == '__main__':
    main()

