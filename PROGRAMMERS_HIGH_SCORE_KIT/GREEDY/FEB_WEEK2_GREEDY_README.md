## [체육복](https://school.programmers.co.kr/learn/courses/30/lessons/42862)

#### 소요시간
- 대략 1시간

#### 간단 풀이 방식
- 도난당한 학생 리스트 `lost`와 여벌의 체육복을 가져온 학생 리스트 `reserve`를 정렬
- `lost`와 `reserve`에 동시에 있는 학생을 `lost`와 `reserve`에서 제거
- `student` set에 체육복을 잃어버리지 않은 학생들을 저장
- `reserve`에 있는 학생들을 대상으로 앞뒤 index에 잃어버린 학생이 있다면 빌려주기

#### Pseudo Code
```
function solution(n, lost, reserve):
  Sort lost and reserve lists
  For each student in lost:
    If student is also in reserve:
      Remove student from both lost and reserve

  students = set()
  Count students who can borrow a uniform
  For each student in reserve:
    If student - 1 is in lost:
      add student -1 in students
      Increment borrow_count
      Remove student - 1 from reserve
    Else if student + 1 is in lost:
      add student +1 in students
      Remove student + 1 from reserve
  Return len(students)
```

#### 시간복잡도
- 종합 : __O(N^2)__

#### 실행시간 및 메모리
- 최소 : `0.01ms`, `10.1MB`
- 최대 : `0.03ms`, `10.2MB`

## [조이스틱](https://school.programmers.co.kr/learn/courses/30/lessons/42860)

#### 소요시간
- 아직 못 품

#### 간단 풀이 방식
- ㅜ

#### Pseudo Code
```

```

#### 시간복잡도

#### 실행시간 및 메모리
- 최소 :
- 최대 :

## [큰 수 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/42883)

#### 소요시간
- 하루종일

#### 간단 풀이 방식
- `number` 문자열의 각 숫자를 순회하면서 현재 숫자가 스택의 맨 윗 숫자보다 큰지 비교
    - 만약 크다면
        - `stack`의 맨 윗 숫자를 제거, k -= 1
        - `stack`의 맨 윗숫자가 현재 숫자보다 클때까지 위과정을 반복
    - 만약 작다면 `continue`
- 현재 숫자를 `stack`에 `append`
- `stack`에서 (전체 길이 - k)만큼을 문자열로 만들어서 리턴

#### 시도했던 내용들
**TRY 1**
1. 현재 숫자보다 큰 숫자(`b`)를 뒤에서 찾음
2. `b` 뒤에 남아있는 숫자 중에서 현재 숫자보다 작은 숫자의 개수를 count  
    2-1. `전체길이 - k`를 보장한다면 현재 숫자를 제거  
    2-2. 보장하지 않는다면, 현재 숫자를 보류, `k-=1`

**TRY 2**
1. `number`에서 `k` 길이 문자열들을 생성  
    ex) `number` = "1234", `k` = 2 라면 "12", "23", "34"
2. 문자열들 중 가장 큰 숫자의 첫번째 숫자를 `answer`에 저장  
    ex) `answer` = "3"
3. `k -= 가장 큰 숫자의 index`  
    ex) 가장 큰 숫자 "34"의 index가 2이기 때문에, 2개의 숫자가 제거된 것과 같으므로 `k -= 2`
4. `k`가 0이 될때까지 1-3까지의 과정을 반복

-> 위 풀이는 가장 큰 숫자가 인덱스가 0인경우 `k`가 감소되지 않아 무한루프를 도는 경우 발생  
-> 그렇다고 `k -= max(1, 가장 큰 숫자의 index)`를 하자니 옳지 않은 풀이가 됨

#### Pseudo Code
```
function solution(number, k):
  answer = empty stack

  for each digit in number:
    while k > 0 and answer is not empty and last element of answer < current digit:
      remove last element from answer
      k = k - 1
    add current digit to answer

  return string formed by joining elements of answer from index 0 to length(answer) - k - 1
```

#### 시간복잡도
- __O(N^2)__

#### 실행시간 및 메모리
- 최소 : `0.01ms`, `10MB`
- 최대 : `93.75ms`, `14.9MB`

## [구명보트](https://school.programmers.co.kr/learn/courses/30/lessons/42885)

#### 소요시간
- 대략 30분

#### 간단 풀이 방식
- `people`을 정렬
- 가장 가벼운 사람과 가장 무거운 사람의 몸무게 합이 limit을 초과하는지 확인
    - 초과한다면 `right index를 -= 1`, `answer += 1`(무거운 사람 혼자 탑승)
    - 초과하지 않는다면 `right index를 -= 1`, `left index를 += 1`, `answer += 1` (두 사람이 동시에 탑승)
- `left index`가 `right index` 이하일때까지 위 과정을 반복

#### Pseudo Code
```
unction solution(people, limit):
  answer = 0

  sort people list in ascending order

  left_idx = 0
  right_idx = length of people - 1

  while left_idx <= right_idx:
    if people[left_idx] + people[right_idx] > limit:
      right_idx = right_idx - 1
    else:
      right_idx = right_idx - 1
      left_idx = left_idx + 1
    answer = answer + 1

  return answer
```

#### 시간복잡도
- __O(N log N)__

#### 실행시간 및 메모리
- 최소 : `0.01ms`, `10MB`
- 최대 : `8.92ms`, `10.6MB`

## [섬 연결하기](https://school.programmers.co.kr/learn/courses/30/lessons/42861)

#### 소요시간
- 하루 종일

#### 간단 풀이 방식
- 크루스칼 알고리즘 활용(모든 정점을 포함하고, 사이클이 없는 연결 선을 그었을 떄, 가중치의 합이 최소가 되는 상황을 구함)
- 다리의 정보를 가지고 있는 `costs`를 비용을 기준으로 정렬(오름차순)
- `link` set을 생성한 후, `costs`의 `start` 섬을 저장
- `len(link)`가 섬의 개수와 같아질때까지 아래 과정을 반복
    - 출발 섬과 도착 섬이 모두 `link`에 있는 경우 continue
    - 출발 섬과 도착 섬 중 하나가 `link`에 없는 경우 `link`에 출발섬, 도착섬을 추가 & `answer += 비용`

#### 시도했던 내용들
**TRY 1**
- `count_total_node(counts)` : 다리 정보를 입력받아 노드들의 총 개수를 구하여 전역변수 `totalNum`에 저장
- `dfs(cur_idx, sum_costs, costs, bridge_list)`
    * `brdige_list` : 현재까지 연결된 섬들을 저장하는 리스트
    - `len(set(bridge_list)) == totalNum`이면 return
    - `costs[cur_idx]`의 정보를 가져와 시작섬과 도착섬 중 `bridge_list`에 없는 섬이 존재한다면 `brdige_list`에 두 섬 모두 추가
    - dfs 호출
    - `bridge_list`에 넣었던 시작섬, 도착섬 제거

**TRY 2**
- TRY1과 유사하지만, `brdige_list`가 아니라 `bridge_map`을 활용
- `bridge_map`과 `start_index`를 입력받아 연결된 섬들의 개수를 계산하는 함수(`count_connected_island`) 활용
- `count_connected_island`의 결과값이 `totalNum`일때까지 dfs 반복
-> dfs를 활용하다보니 특정 다리값을 넣어보지 못하는 현상 발생

#### Pseudo Code
```
function solution(n, costs):
  answer = 0

  sort costs list by cost in ascending order

  link = set containing the first island in costs

  while length of link is not equal to n:
    for each bridge in costs:
      if both islands of bridge are in link:
        continue
      if either island of bridge is in link:
        add both islands of bridge to link
        add cost of bridge to answer
        break

  return answer
```

#### 시간복잡도
- __O(N log N)__

#### 실행시간 및 메모리
- 최소 : `0.01ms`, `10.2MB`
- 최대 : `0.05ms`, `10.2MB`

## [단속카메라](https://school.programmers.co.kr/learn/courses/30/lessons/42884)

#### 소요시간
- 대략 30분

#### 간단 풀이 방식
- 차량의 이동경로를 담은 `routes`를 진입 시점을 기준으로 정렬
- 가장 첫 차량의 진입시점의 카메라 설치
- `routes`를 순회하면서 카메라의 진입시점과 진출시점 사이에 카메라가 존재하지 않으면 진출시점에 카메라 설치

#### Pseudo Code
```
function solution(routes):
  sort routes list by entry point in ascending order

  answer = 1
  cur_camera = entry point of the first route

  for each route from the second to the last:
    if current route's entry point >= cur_camera and entry point <= current route's exit point
      answer = answer + 1
      cur_camera = exit point of the current route

  return answer
```

#### 시간복잡도
- __O(n log n)__

#### 실행시간 및 메모리
- 최소 : `0.01ms`, `10.2MB`
- 최대 : `1.13ms`, `10.5MB`