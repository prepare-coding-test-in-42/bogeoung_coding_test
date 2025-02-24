# DP
## [N으로 표현](https://school.programmers.co.kr/learn/courses/30/lessons/42895)

#### 소요시간
- 2시간 + 구글링

#### 간단 풀이 방식
- `set_list`에 각 연산 단게에서 만들 수 있는 숫자들의 집합을 저장
- `i-1`번째에 있는 `set_list`를 활용해 만들 수 있는 숫자의 집합들을 `i`번쨰 `set_list`에 저장

#### Pseudo Code
```
def solution(N, number):
    if number == 1:
        return 1
    
    set_list = []
    
    for cnt in range(1,9):
        part_set = set()
        part_set.add(int(str(N)*cnt)) 
        for i in range(cnt -1):
            for op1 in set_list[i]:
                for op2 in set_list[cnt-i-2]:
                    part_set.add(op1 + op2)
                    part_set.add(op1 - op2)
                    part_set.add(op2 - op1)
                    part_set.add(op1 * op2)
                    if op2 != 0:
                        part_set.add(op1 / op2)
        
        if number in part_set:
            return cnt
        set_list.append(part_set)
        
    return -1
```

#### 시간복잡도
- _O(N^2)_

#### 실행시간 및 메모리
- 최소 : `0.02ms`, `10.4MB`
- 최대 : `114.17ms`, `15.4MB`


## [정수 삼각형](https://school.programmers.co.kr/learn/courses/30/lessons/43105)

#### 소요시간
- 30분

#### 간단 풀이 방식
- 현재 좌표가 `[i][j]`라고 할 때 `max([i-1][j], [i][j-1])`에 현재값을 더하기

#### Pseudo Code
```
def solution(triangle):
    
    for i in range(1,len(triangle)): # 행
        for j in range(len(triangle[i])): # 열
            if j == 0:
                triangle[i][j] = triangle[i-1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
            else:
                triangle[i][j] = max(triangle[i-1][j], triangle[i-1][j-1]) + triangle[i][j]
    
    answer = max(triangle[-1])
    
    return answer
```

#### 시간복잡도
- _O(N^2)_

#### 실행시간 및 메모리
- 최소 : `0.01ms`, `10.2MB`
- 최대 : `52.22ms`, `14.1MB`


## [등굣길](https://school.programmers.co.kr/learn/courses/30/lessons/42898)

#### 소요시간
- 45분

#### 간단 풀이 방식
- 현재 좌표까지 도착할 수 있는 경로의 수를 저장
    - 오른쪽이랑 아래로밖에 움직일 수 없기 때문에 최소 경로가 보장되기 때문

#### Pseudo Code
```
def solution(m, n, puddles):
    map = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n): # 행
        for j in range(m): # 열
            if i == 0 and j == 0:
                map[i][j] = 1
            elif [j+1, i+1] in puddles:
                continue
            elif j == 0:
                map[i][j] = map[i-1][j]
            elif i == 0:
                map[i][j] = map[i][j-1]
            else:
                map[i][j] = map[i-1][j] +  map[i][j-1]
    
    return map[i][j] % 1000000007
    
```

#### 시간복잡도
- _O(N^3)_

#### 실행시간 및 메모리
- 최소 : `1.04ms`, `10.3MB`
- 최대 : `4.15ms`, `10.3MB`

## [사칙연산](https://school.programmers.co.kr/learn/courses/30/lessons/1843)

#### 소요시간
- X

#### 간단 풀이 방식
- 

#### Pseudo Code
```
    
```

#### 시간복잡도
-

#### 실행시간 및 메모리
- 최소 :
- 최대 :

## [도둑질](https://school.programmers.co.kr/learn/courses/30/lessons/42897)

#### 소요시간
- 30분 + 검색

#### 간단 풀이 방식
- 처음집부터 털되 `i번째 집 + i-2번째집을 턴 money`와 `i-1번째 집을 터는것의 money`를 비교해서 큰 것을 턴 값을 dp에 저장
- `처음집을 털고, 마지막집을 털지 않는 경우`, `처음집을 털지 않고, 마지막집을 터는 경우` 2가지를 비교

#### Pseudo Code
```
def solution(money):
    dp1 = [0] * len(money)
    dp2 = [0] * len(money)

    dp1[0] = money[0]
    for i in range(1, len(money) - 1):  # 첫번째 집을 털고, 마지막 집을 털지 않는 경우
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])

    dp2[0] = 0
    for i in range(1, len(money)):      # 첫번째 집은 털지 않고, 마지막 집을 터는 경우
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

    return max(dp1[-2], dp2[-1])
 
```

#### 시간복잡도
- _O(N)_

#### 실행시간 및 메모리
- 최소 : `0.03ms`, `10.2MB`
- 최대 : `576.99ms`, `90.4MB`