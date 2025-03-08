## [구슬 탈출 2](https://www.acmicpc.net/problem/13460)

#### 소요시간
- 1시간 + 검색

#### 간단 풀이 방식
- 보드의 크기와 보드를 입력받는다.
- 색깔 구슬(빨강, 파랑)의 위치들을 구한다.
- BFS로 구슬을 이동시킨다.
  - 빨강 구슬이 구멍에 도착하면 현재까지의 이동 횟수를 출력한다.
  - 파란 구슬이 구멍에 도착하면, 해당 케이스는 bfs를 더 이상 실행하지 않는다.
  - 빨간 구슬과 파란 구슬이 동일한 칸에 도착한 경우, 더 멀리 이동한 구슬을 한칸 뒤로 이동시킨다(이동 해온 방향의 반대방향으로)
  - 이동한 구슬의 새로운 위치와 이동 횟수를 큐에 추가한다.
- 10번의 이동 후에도 빨간 구슬이 구멍에 도착할 수 없으면 -1을 출력한다.

#### Pseudo Code
```
function input_func():
    Read n, m
    Create board from input

function find_color_bead(board):
    Find locations of red and blue beads

function move(x, y, direction, board):
    Move bead in the given direction until it hits a wall or a hole, return new position and count of moves

function run(r_loc, b_loc, board):
    Initialize visited list and queue
    While queue is not empty:
        For each direction:
            Move both beads, handle special cases where they meet, and check for success
            If a bead falls into the hole, print count and exit
            If not visited, add the new state to the queue

function main():
    Read input, find bead locations, and run BFS

```

#### 시간복잡도
- `input_func` : __O(N^2)__
- `find_color_bead` : __O(N^2)__
- 

#### 실행시간 및 메모리
- 메모리 : 35068 KB
- 시간 : 56 ms

## [2048(Easy)](https://www.acmicpc.net/problem/12100)

#### 소요시간
- 1시간 + chatgpt의 힌트 

#### 간단 풀이 방식
- 정사각형 보드를 입력받는다(맵의 크기와 초기값). 
- 주어진 방향에 따라 타일을 이동시킨다. 
  - 이동한 타일이 벽에 닿으면 더 이상 이동하지 않는다. 
  - 이동한 타일이 다른 타일과 동일한 값이면 두 타일을 합친다(2배로 커진다). 
  - 타일이 합쳐진 후에는 해당 위치에 더 이상 이동할 수 없다. 
  - 사라진 타일은 0으로 처리된다. 
- 타일을 이동시키고 병합하는 과정을 반복하여, 보드에 가능한 한 큰 값을 만들어낸다. 
- 최대 5번의 이동을 수행하며, 그 중 가장 큰 타일 값을 구한다.
- (73% 실패) 98번째 라인에 이동 전 보드와 이동 후 보드가 같다면 dfs를 수행하지 않는 코드를 작성하였는데, 해당 코드가 존재하면 depth가 5에 도달하지 못하는 경우가 존재하여, max_value가 초기값인 0이 되는 경우가 존재하였다.

#### Pseudo Code
```
function init_board():
    n = read integer input()
    board = read 2D list of size n x n
    return board

function move_board(board, direction):
    for each cell in the board:
        move the tile according to direction
        merge if same tiles are encountered
    return new board

function dfs(board, depth):
    if depth == 5:
        update max_value
        return
    for each direction:
        new_board = move_board(board, direction)
        dfs(new_board, depth + 1)

function main():
    board = init_board()
    dfs(board, 0)
    print max_value

```

#### 시간복잡도
- `init_board` : __O(N^2)__
- `move_board` : __O(N^2)__
- `dfs` : __O(4^5 * n^2)__ = __O(1024 * N^2)__
  * 최대 5번의 깊이 우선탐색, 각 깊이에서 4개의 방향을 탐색
  * board의 크기 `n * n`
- 종합 : __O(1024 * N^2)__

#### 실행시간 및 메모리
- 메모리 : 33696 KB
- 시간 : 572 ms

## [뱀](https://www.acmicpc.net/problem/3190)

#### 소요시간
- 2시간

#### 간단 풀이 방식
- 정사각 보드를 입력받는다(맵의 크기, 사과의 위치)
- 뱀의 머리 위치를 해당 방향 정보로 이동시킨다.(초기값은 우측으로 이동한다.)
  - 이동한 머리가 벽에 닿는다면 현재까지의 시간을 반환한다.
  - 이동한 머리가 뱀의 몸에 닿는다면 현재까지의 시간을 반환한다.
  - 이동한 머리에 사과가 존재한다면 뱀의 위치 정보를 담고있는 `snake_queue`에 현재 머리 위치를 0번째에 추가한다.
  - 이동한 머리에 사과가 존재하지 않는다면 `snake_queue`의 마지막 index 값을 제거하고, 현재 머리 위치를 0번째에 추가한다.
- 뱀의 머리가 벽에 닿거나, 몸에 닿을때까지 첫번째 과정을 반복한다. 

#### Pseudo Code
```
function init_board():
    n = read integer input()  // Read board size
    k = read integer input()  // Read number of apples
    board = create n x n grid initialized with 0
    
    for i = 0 to k-1:
        x, y = read apple coordinates
        set board[x-1][y-1] = 1  // Place apple on board
        
    l = read integer input()  // Read number of moves
    l_list = empty list
    for i = 0 to l-1:
        time, direction = read move time and direction
        append (time, direction) to l_list
    return board, l_list

function update_move_direction(cur_move_direction_index, char):
    if char is "D": increment cur_move_direction_index
    if char is "L": decrement cur_move_direction_index
    normalize cur_move_direction_index to stay within [0, 3]
    return cur_move_direction_index

function run(board, l_list):
    set move_direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]  // Directions: right, down, left, up
    set snake_queue to [starting position]
    time = 0
    while true:
        increment time
        calculate new snake head position
        if head hits wall or body: return time
        if apple is at new head position: grow snake, remove apple
        else: move snake forward
        update snake position
        if time matches move time in l_list: change direction

function main():
    board, l_list = init_board()
    result = run(board, l_list)
    print result

```

#### 시간복잡도
- `init_board` : __O(N^2)__
- `run` : __O(N^3)__
  * 몸의 길이는 최대 `n*n`까지 늘어날 수 있기 때문
  * `insert(0)`, `pop` 은 __O(N)__이기 때문
- 종합 : __O(N^3)__

#### 실행시간 및 메모리
- 메모리 : 32412 KB
- 시간 : 40 ms