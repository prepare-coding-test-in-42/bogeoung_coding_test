## [연구소3](https://www.acmicpc.net/problem/17142)

#### 소요시간
- 1시간 30분 가량

#### 간단 풀이 방식
- 문제 그대로 풀이

#### 헤맸던 부분
- 비활성화된 바이러스와 벽과의 차이점을 구분을 못해서 헤맴

#### Pseudo Code
```
def spread_virus(lab_map, remain_count):
    queue = deque()

    for x, y in find_num_in_map(lab_map, 0):
        queue.append([x, y, 0])

    while queue:
        x, y, time = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if lab_map[nx][ny] in [-1, '*']:
                    if lab_map[nx][ny] == -1:
                        remain_count -= 1
                    lab_map[nx][ny] = time + 1
                    queue.append([nx, ny, time + 1])

                if remain_count <= 0:
                    return time + 1
    if remain_count > 0:
        return -1

    return 0
```

#### 시간복잡도
- 

#### 소요시간 및 메모리
- 메모리 : 36284 KB
- 소요시간 : 680 ms

## [상어 초등학교](https://www.acmicpc.net/problem/21608)

#### 소요시간
- 2시간

#### 간단 풀이 방식
- 문제 요구사항대로 풀이

#### 헤맸던 부분
- 만약 좋아하는 친구가 이미 앉았더라면, 친구 위치 기준 4군데 위치에 대해서만 탐색을 수행하도록 했는데, 오류를 발견하지 못해서 헤맴
- 결국 모든 자리에 대해서 탐색하는 코드로 변경
- 추후 위 코드의 문제점을 발견하여 수정했더니 시간이 100ms가량 감소

#### Pseudo Code
```
def find_loc(student_fav, school, added_students):
    if len(added_students) > 0:
        count_only_location = defaultdict(int)
        for added_student, row, col in added_students:
            if added_student in student_fav:
                for direction in near_directions:
                    new_row, new_col = row + direction[0], col + direction[1]
                    if 0 <= new_row < n and 0 <= new_col < n and school[new_row][new_col] == 0:
                        count_only_location[(new_row, new_col)] += 1

        if len(count_only_location) > 0:
            calc_location = dict()
            for loc, count in count_only_location.items():
                calc_location[loc] = [count, count_empty_space(loc[0], loc[1], school)]
            sorted_calc_location = sorted(calc_location.items(), key=lambda x: [-x[1][0], -x[1][1], x[0][0], x[0][1]])
            return sorted_calc_location[0][0]

    candidate_loc = dict()
    for i in range(n):
        for j in range(n):
            if school[i][j] == 0:
                candidate_loc[(i, j)] = count_empty_space(i, j, school)

    sorted_candidate_loc = sorted(candidate_loc.items(), key=lambda x: [-x[1], x[0][0], x[0][1]])
    return sorted_candidate_loc[0][0]
```

#### 시간복잡도
- `main` : $O(N^2)$
- `find_loc` : 최악의 경우 $O(N^2 \cdot logN)$
- 종합 : $O(N^4)$ ~ $O(N^4 \cdot log N)$
#### 소요시간 및 메모리
- 메모리 : 35232 KB
- 소요시간 : 116 ms
