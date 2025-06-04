## [아기 상어](https://www.acmicpc.net/problem/16236)

#### 소요시간
- 약 1시간

#### 간단 풀이 방식
- bfs를 활용하여 가장 가까운 거리에 있는 먹을 수 있는 상어를 찾음

- 헤맨 부분
    - bfs가 최단거리를 보장하는 것을 잊고, dfs를 활용했다가 오히려 코드가 복잡해졌음.

#### Pseudo Code
```
def bfs(n, sea_map, shark):
    visited = [[-1] * n for _ in range(n)]
    queue = deque()
    queue.append((shark.x, shark.y))
    visited[shark.x][shark.y] = 0

    fish_list = []
    min_dist = sys.maxsize
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # 위 -> 왼 -> 오 -> 아래 우선순위

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n:
                # 방문하지 않았고, 상어 크기 이하로 이동 가능
                if visited[nx][ny] == -1 and sea_map[nx][ny] <= shark.age:
                    visited[nx][ny] = visited[x][y] + 1
                    # 먹을 수 있는 물고기 발견
                    if 0 < sea_map[nx][ny] < shark.age:
                        distance = visited[nx][ny]
                        if distance < min_dist:
                            fish_list = [(nx, ny, distance)]
                            min_dist = distance
                        elif distance == min_dist:
                            fish_list.append((nx, ny, distance))
                    else:
                        queue.append((nx, ny))
```

#### 시간복잡도
- `bfs` : $O(N^2)$
- `run` : 최대 N
- 종합 : 최악 $O(N^3)$

#### 소요시간 및 메모리
- 메모리 : 35076 KB
- 소요시간 : 92 ms

## [미세먼지 안녕!](https://www.acmicpc.net/problem/17144)

#### 소요시간
- 아직 해결 못함.

#### 간단 풀이 방식
- 간단 풀이 방식을 작성합니다.

#### Pseudo Code
```

```

#### 시간복잡도
- 시간복잡도를 작성합니다.

#### 소요시간 및 메모리 (**PyPy3 기준**, PyPy3가 사용되지 않았다면 괄호를 제거합니다.)
- 메모리 : x KB
- 소요시간 : x ms

## [낚시왕](https://www.acmicpc.net/problem/17143)

#### 소요시간
- 2시간 이상.. 아직 시간초과 해결 안됨

#### 간단 풀이 방식
- 간단 풀이 방식을 작성합니다.

#### Pseudo Code
```

```

#### 시간복잡도
- 시간복잡도를 작성합니다.

#### 소요시간 및 메모리 (**PyPy3 기준**, PyPy3가 사용되지 않았다면 괄호를 제거합니다.)
- 메모리 : x KB
- 소요시간 : x ms
