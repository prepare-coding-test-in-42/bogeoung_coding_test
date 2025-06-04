## [퇴사](https://www.acmicpc.net/problem/14501)

#### 소요시간
- 30분

#### 간단 풀이 방식
- 각 날짜별 최대 수익을 `result`에 기록
- 각 일정을 돌면서 result[상담이 끝나는 날]을 업데이트
- 만약 result[상담이 끝나는 날]의 값이 비어있지 않다면 해당 값과 result[상담이 시작하는 날] + 현재 상담의 수익 값을 비교하여 더 큰 값으로 업데이트
- result [-1]을 출력

#### Pseudo Code
```
N = len(arr)
result = [0 for i in range(N + 1)]
for i in range(len(arr)):
    # i번째 상담을 했을 때 상담기간 내에 끝나는 날만 확인
    for j in range(i + arr[i][0], N + 1):
        # j를 기준으로 상담했을 때, 얻는 최대 수익 저장
        if result[j] < result[i] + arr[i][1]:
            result[j] = result[i] + arr[i][1]
print(result[-1])
```

#### 시간복잡도
- O(N^2)

#### 실행시간 및 메모리
- 메모리 : 34140 KB
- 시간 : 68 ms

## [연구소](https://www.acmicpc.net/problem/14502)

#### 소요시간
- 1시간 30분

#### 간단 풀이 방식
- 백트래킹을 활용해서 벽을 세울 수 있는 가능한 조합을 모두 탐색

#### Pseudo Code
```
def run(lab, added_wall_count):
    global answer
    if added_wall_count == 3:
        lab.spread_virus()
        answer = max(answer, lab.count_safety_space())
        return

    for i in range(lab.n):
        for j in range(lab.m):
            if lab.map[i][j] == 0:
                lab.make_wall(i, j)
                run(lab, added_wall_count + 1)
                lab.break_wall(i, j)

```

#### 시간복잡도
- $O((n\cdot m) ^ 4)$

#### 실행시간 및 메모리
- 메모리 : 122492 KB
- 시간 : 2896 ms