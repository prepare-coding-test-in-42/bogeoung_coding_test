## [시험 감독](https://www.acmicpc.net/problem/13458)

#### 소요시간
- 10분

#### 간단 풀이 방식
- 시험장의 개수(`n`), 각 시험장에 있는 응시자의 수(`a`), 총감독관이 감시할 수 있는 응시자 수(`b`), 부감독관이 감시할 수 있는 응시자 수(`c`)를 입력 받는다.
- 필요한 감독관의 최소 수 `answer`를 시험장의 개수 `n`으로 초기화 한다.
- 모든 시험장에 대해서 `a` - `b`를 `c`로 나눈 몫을 `answer`에 더한다. 
  - 나머지가 존재한다면 `answer`에 1을 더한다.


#### Pseudo Code
```
FUNCTION init_func():
    Read an integer `n` from input
    Read a list `a` of `n` integers from input
    Read two integers `b` and `c` from input
    RETURN n, a, b, c

FUNCTION main():
    CALL init_func() and store results in `n, a, b, c`
    Initialize `answer` with `n` (each examinee needs at least one supervisor)

    FOR i from 0 to n-1:
        Calculate `cur_examinee` as `a[i] - b` (remaining students after head supervisor)
        
        IF `cur_examinee < 0`:
            CONTINUE (No additional sub-supervisors needed)
        
        IF `cur_examinee % c != 0`:
            Increment `answer` by 1 (For any remaining students that do not fit evenly)
        
        Increment `answer` by `cur_examinee // c` (Number of sub-supervisors required)
    
    PRINT `answer`

IF script is run directly:
    CALL `main()`

```

#### 시간복잡도
- __O(N)__

#### 실행시간 및 메모리
- 메모리 : 129196 KB
- 시간 : 432 ms

## [주사위 굴리기](https://www.acmicpc.net/problem/14499)

#### 소요시간
- 45분

#### 간단 풀이 방식
- 지도의 세로 크기(`n`), 가로크기(`m`), 주사위를 놓은 곳의 좌표(`x`,`y`), 명령의 개수(`k`)를 입력받는다. 
- 지도의 정보(`board`)와 `k`개의 명령(`command`)을 입력받는다. 
- 주사위의 값을 나타내는 `dice_list`를 0으로 채워진 길이 6의 리스트로 초기화 한다.
- 이동하는 명령에 따라 아래 과정을 수행한다.
  - 예정되는 새로운 좌표(`new_x`, `new_y`)를 구한다.
  - 새로운 좌표가 지도를 나가면 아무것도 수행하지 않는다.
  - `board[new_x][new_y]`의 값이 0이라면 
    - `dice_list[5]`의 값을 `board[new_x][new_y]`에 업데이트한다.
  - `board[new_x][new_y]`의 값이 0이 아니라면 
    - `board[new_x][new_y]`의 값을 `dice_list[5]`에 업데이트한다.
    - `board[new_x][new_y]`의 값을 0으로 초기화 한다. 
  - 현재 주사위의 윗면에 쓰여 있는 수(`dice_list[0]`)을 출력한다.


#### Pseudo Code
```
GLOBAL VARIABLES: n, m, x, y initialized to 0

FUNCTION input_func():
    Read n, m, x, y, k from input
    Create a 2D list `board` of size n × m, initializing all values to 0
    Populate `board` with input values
    Read `commands` list from input
    RETURN board, commands

FUNCTION move(dice_list, move_index):
    IF move_index is 1 (East):
        Rotate dice list accordingly
    IF move_index is 2 (West):
        Rotate dice list accordingly
    IF move_index is 3 (North):
        Rotate dice list accordingly
    IF move_index is 4 (South):
        Rotate dice list accordingly
    RETURN updated dice_list

FUNCTION run(board, commands):
    Initialize dice_list with 6 zeros
    Define move_direction for East, West, North, and South
    SET cur_x and cur_y as initial x and y

    FOR each command in commands:
        Compute new_x and new_y based on move_direction
        IF new position is within bounds:
            Update dice_list using move() function
            IF board[new_x][new_y] is 0:
                Copy dice’s bottom value to board[new_x][new_y]
            ELSE:
                Copy board[new_x][new_y] value to dice's bottom and set board[new_x][new_y] to 0
            Print the top value of the dice
            Update cur_x, cur_y to new_x, new_y

FUNCTION main():
    Get board and commands from input_func()
    Run the simulation using run(board, commands)

IF script is executed directly:
    CALL main()

```

#### 시간복잡도
- `input_func` : __O(N*M)__
- `run` : __O(K)__
- 종합 : __O(N*M+K)__

#### 실행시간 및 메모리
- 메모리 : 32412 KB
- 시간 : 36 ms

## [테트로미노](https://www.acmicpc.net/problem/14500)

#### 소요시간
- 45분

#### 간단 풀이 방식
- 보드를 입력받고, 테트로미노의 좌표를 정의한다.
- 보드의 모든 좌표에서 테트로미노를 배치해본다.
  - 테트로미노의 모든 좌표가 보드 내에 존재한다면 모든 좌표의 합을 구한다.
  - 모든 좌표의 합 중 최대값을 저장한다.
- 보드를 90도씩 돌려가며 직전의 과정을 반복하며 최대값을 갱신한다.
- 최대값을 출력한다.
- (보드를 회전시켰을 때 N과 M을 교환하는 부분, tetromino의 대칭 좌표를 추가해야하는 부분에서 시간이 추가로 소요됐다.) 


#### Code
```
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

```

#### 시간복잡도
- __O(NM)__
  - `N`, `M` : 입력받은 보드의 크기 

#### 실행시간 및 메모리
- 메모리 : 41820 KB
- 시간 : 6252 ms