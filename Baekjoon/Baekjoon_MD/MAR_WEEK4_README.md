## [로봇청소기](https://www.acmicpc.net/problem/14503)

#### 소요시간
- 1시간 30분

#### 간단 풀이 방식
- 문제 그대로 구현
- 헷갈렸던 부분에서 시간 소요가 많이 되었으며, 헷갈렸던 내용은 아래와 같음.
  1. 입력으로 받은 1은 벽이였다.
  2. 청소 처리에 대한 여부를 1로 채웠는데, 벽과 동일한 숫자였기 때문에 로봇청소기의 움직임을 제한하게 되었다.

#### Pseudo Code
```
def run(n, m, robot, room_map):
    while True:
        if room_map[robot.x][robot.y] == 0:
            room_map[robot.x][robot.y] = -(robot.clean_count + 1)
            robot.clean_count += 1

        nearby_coordinates = robot.get_4direction_coordinate() # 현재 좌표 기준 4방향의 좌표들
        is_cleaned_nearby_coordinates = [1, 1, 1, 1]
        for idx, coordinate in enumerate(nearby_coordinates):
            if 0 <= coordinate[0] < n and 0 <= coordinate[1] < m:
                if room_map[coordinate[0]][coordinate[1]] != 0:
                    is_cleaned_nearby_coordinates[idx] = 1
                else:
                    is_cleaned_nearby_coordinates[idx] = room_map[coordinate[0]][coordinate[1]]

        if sum(is_cleaned_nearby_coordinates) == 4: # 청소되지 않은 빈 칸이 없는 경우
            move_x, move_y = nearby_coordinates[(robot.d + 2) % 4]
            if not(0 <= move_x < n and 0 <= move_y < m):
                return
            elif room_map[move_x][move_y] == 1:
                return
            else:
                robot.x, robot.y = move_x, move_y

        elif sum(is_cleaned_nearby_coordinates) != 4: # 청소되지 않은 빈 칸이 있는 경우
            while True:
                robot.rotate_counter_clockwise_90()
                front_coordinate = nearby_coordinates[robot.d]
                if room_map[front_coordinate[0]][front_coordinate[1]] == 0:
                    robot.x, robot.y = front_coordinate[0], front_coordinate[1]
                    break

```

#### 시간복잡도
- O(N^2)

#### 실행시간 및 메모리
- 메모리 : 34140 KB
- 시간 : 68 ms

## [연산자 끼워넣기](https://www.acmicpc.net/problem/14888)

#### 소요시간
- 30분 이내

#### 간단 풀이 방식
- dfs를 활용하여 가능한 모든 조합을 탐색

#### Pseudo Code
```
def solution(n, sum, num_arr, opr_arr):
    global max_num, min_num
    if n == len(num_arr):
        max_num = max(sum, max_num)
        min_num = min(sum, min_num)
    for i in range(4):
        if opr_arr[i] == 0:
            continue
        opr_arr[i] -= 1
        solution(n+1, opr_func(sum, num_arr[n], i), num_arr, opr_arr)
        opr_arr[i] += 1

```

#### 시간복잡도
- $O((n-1)!)$ *n은 연산자의 개수

#### 실행시간 및 메모리
- 메모리 : 31256 KB
- 시간 : 92 ms