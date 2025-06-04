## [스타트택시](https://www.acmicpc.net/problem/19238)

#### 소요시간
- 약 1시간

#### 간단 풀이 방식
- 택시의 현재 위치로부터 모든지점까지의 거리를 `dist_map`에 저장.
- 가장 짧은 거리의 손님부터 택시까지 태우는 것을 반복
- `손님을 태울 수 없는 경우`, `손님을 태웠지만 목적지에 도착할 수 없는 경우`, `손님을 태우러 가는 도중 연료가 떨어지는 경우`, `손님을 이동시키는 중에 연료가 떨어지는 경우`에 대해서 예외 처리

#### Pseudo Code
```
def calc_distance(road_map, cur_x, cur_y):
    queue = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]
    move_directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    dist_map = [[0 for _ in range(n)] for _ in range(n)]
    queue.append([cur_x, cur_y, 0])
    while queue:
        cur_x, cur_y,cur_move_count = queue.popleft()
        visited[cur_x][cur_y] = True
        dist_map[cur_x][cur_y] = cur_move_count
        for direction in move_directions:
            new_x, new_y = cur_x + direction[0], cur_y + direction[1]
            if 0 <= new_x < n and 0 <= new_y < n and road_map[new_x][new_y] == 0 and visited[new_x][new_y] == False:
                visited[new_x][new_y] = True
                queue.append([new_x, new_y, cur_move_count + 1])
    return dist_map

def pick_customer(road_map,taxi_x, taxi_y, customers):
    distances = []
    dist_map = calc_distance(road_map, taxi_x, taxi_y)
    for idx, customer in enumerate(customers):
        if customer.x == taxi_x and customer.y == taxi_y:
            distances.append(0)
        elif dist_map[customer.x][customer.y] == 0:
            distances.append(n*n*2)
        else:
            distances.append(dist_map[customer.x][customer.y])

    min_distance = min(distances)
    if min_distance != n*n*2:
        for idx, distance in enumerate(distances):
            if distance == min_distance:
                return [customers.pop(idx), distance]
    return [0, 0]
```

#### 시간복잡도
- `calc_distance` : $O(n^2)$
- 종합 : $O(N^2 \cdot m)$  *m은 손님의 수

#### 소요시간 및 메모리
- 메모리 : 35148 KB
- 소요시간 : 324 ms

## [상어 중학교](https://www.acmicpc.net/problem/21609)

#### 소요시간
- 약 2시간

#### 간단 풀이 방식
- 문제 그대로 구현

#### 헤맸던 부분
- 그룹에 속한 블록의 개수가 2개 이상이여한다는 부분을 놓쳐서 예제 이해가 안되서 헤맴.

#### Pseudo Code
```
def run(block_map):
    answer = 0
    while True:
        #그룹을 찾음
        groups = find_groups(block_map)
        #그룹이 존재하지 않은 경우 break
        if len(groups) <= 0:
            return answer
        # 크기가 가장 큰 그룹을 선정
        selected_group = groups.pop(0)
        if len(selected_group.blocks) < 2:
            return answer
        # 그룹의 크기 ^ 2만큼 점수 획득 & 방문 처리
        answer += selected_group.get_group_size() ** 2
        for block in selected_group.blocks:
            block_map[block[0]][block[1]] = 9

        # 격자에 중력 작용
        apply_gravity(block_map)

        # 격자를 반시계 방향으로 회전
        block_map = rotate_counter_clockwise(block_map)
        # 격자에 중력 작용
        apply_gravity(block_map)
```

#### 시간복잡도
`find_groups` : $O(N^2)$
`rotate_counter_clockwise` : $O(N^2)$
- 종합 :  $O(N^4)$

#### 소요시간 및 메모리 
- 메모리 : 36240 KB
- 소요시간 : 104 ms

## [모노미노도미노 2](https://www.acmicpc.net/problem/20061)

#### 소요시간
- 2시간 이상

#### 간단 풀이 방식
- 문제 대로 구현.
- 다만 빨간 블록은 구현하지 않고, 파란 블록과 초록 블록만 구현함.

#### 헤맸던 부분
1. 블록은 하나의 그룹처럼 이동해야하는데, 1x1 블록을 여러번 이동 시키는 것으로 구현하여 블록 형태가 어긋나는 것이 존재.
2. 반례를 생각하지 못한 부분이 많음
- 모든 칸이 채워진 줄이 2개 이상 동시에 발생할 때
- 연한 색깔의 구역에 2개 이상의 블록이 한번에 추가될 때
3. 파란 영역의 구현을 반시계 방향 회전 & 시계 방향 회전 + 초록 영역의 코드로 구현하려다가 행의 삭제가 열의 삭제와 다르게 동작하는 것을 뒤늦게 인지

#### Pseudo Code
```
def run(orders):
    block_types = [[[0, 0]], [[0, 0]], [[0, 0], [0, 1]], [[0, 0], [1, 0]]]
    blue_blocks = Blue()
    green_blocks = Green()
    score = 0
    for t, x, y in orders:
        green_added_blocks = []
        blue_added_blocks = []
        for direction in block_types[t]:
            green_added_blocks.append([direction[0], y + direction[1]])
            blue_added_blocks.append([x + direction[0], direction[1]])

        green_blocks.add_block(green_added_blocks)
        blue_blocks.add_block(blue_added_blocks)

        score += green_blocks.check_rows()
        score += blue_blocks.check_cols()

        green_blocks.check_light_row()
        blue_blocks.check_light_col()

    return [score, blue_blocks.count_filled_block() + green_blocks.count_filled_block()]
```

#### 시간복잡도
- $O(N)$

#### 소요시간 및 메모리 
- 메모리 : 34456 KB
- 소요시간 : 392 ms
