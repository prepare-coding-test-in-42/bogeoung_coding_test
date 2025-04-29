# BINARYSEARCH
## [입국심사](https://school.programmers.co.kr/learn/courses/30/lessons/43238)

#### 소요시간
- 1시간 + 검색
- 어떻게 풀지 도저히 감이 안잡혀서 검색을 했다. 나는 사람 기준으로 어떻게 이분탐색을 하지? 라는 생각이였는데, 풀이를 검색해보고 나니 시간을 기준으로 이분탐색을 하였다.
시간을 기준으로 이분탐색을 해야한다는 생각을 떠올리는 것이 키 포인트였던 것 같다. 

#### 간단 풀이 방식
- `최소시간(left)`과 `가장 비효율적으로 심사했을 때 걸리는 시간(right)` 사이의 값을 이분 탐색으로 찾는다.
- `mid = (최소시간 + 비효율적으로 심사했을 때 걸리는 시간) // 2` 일 때 `mid` 시간 동안 각 심사원들이 총 몇명의 사람을 심사했는지 구한다.
  - 총 심사한 사람의 수가 n 이상일 때 : right를 mid - 1로 업데이트, answer를 mid값으로 업데이트
  - 총 심사한 사람의 수가 n 미만일 때 : left를 mid + 1로 업데이트 
  
#### Pseudo Code
```
function solution(n, times):
    initialize left = 1
    initialize right = max(times) * n  
    while left <= right:
        mid = (left + right) // 2  

        people = 0  
        for each time in times:
            people += mid // time  

        if people >= n:
            answer = mid  
            right = mid - 1  
        else:
            left = mid + 1 

    return answer  
```

#### 시간복잡도
- __O(log N)__  
  * `N`은 탐색범위의 크기로, 여기서는 `max(times) * n` 이다. 

#### 실행시간 및 메모리
- 최소 : `0.01ms`, `10.2MB`
- 최대 : `469.01ms`, `14.1MB`

## [징검다리](https://school.programmers.co.kr/learn/courses/30/lessons/43236)

#### 소요시간
- 1시간 + 검색
- 돌이 놓아져 있는 지점을 이분탐색 해야한다 생각했지만, 어떻게 해야할지 몰라서 검색
- 찾아보니 위치가 아닌 '바위들 사이의 최소거리 값'에 대해서 이분 탐색을 해야만 했음.
- `distance`의 범위를 보고 이분탐색임을 인지했지만, 이분탐색을 어떤 값에 대해서 적용해야하는지는 좀 더 연습이 많이 필요할 것 같다.

#### 간단 풀이 방식
- 바위들의 위치가 담긴 배열 `rocks`를 정렬
- `left`를 출발지점으로, `right`를 도착지점으로 초기화
- `left > right`가 될때까지 아래 과정을 반복한다.
  - `left`와 `right`의 `mid`값을 반복적으로 구한다. (이 때 mid는 바위들 사이의 최소거리 값이 될 수 있는 후보값이다.)
  - 현재 돌과 이전 돌과의 거리를 계산한다.
  - 계산한 거리가 `mid`보다 작다면 현재 돌을 제거한다. (최소 거리보다 작은 거리가 존재하면 안되기 때문)
  - 제거한 돌의 개수에 따라 `left`,`right`값을 조정한다. 
  
#### Pseudo Code
```
function solution(distance, rocks, n):
    sort rocks
    add distance to rocks 

    left = 1
    right = distance
    answer = 0

    while left <= right:
        mid = (left + right) // 2  
        delete_count = 0
        previous_rock = 0

        for each rock in rocks:
            if rock - previous_rock < mid:
                delete_count += 1  
                if delete_count > n:
                    break 
            else:
                previous_rock = rock  

        if delete_count > n:
            right = mid - 1  
        else:
            answer = mid 
            left = mid + 1

    return answer

```

#### 시간복잡도
- __O(N log N)__

#### 실행시간 및 메모리
- 최소 : `0.00ms`, `10.2MB`
- 최대 : `119.03ms`, `11.7MB`