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

    return answer  // 최종 최소 시간 반환
```

#### 시간복잡도
- __O(log N)__  
  * `N`은 탐색범위의 크기로, 여기서는 `max(times) * n` 이다. 

#### 실행시간 및 메모리
- 최소 : `0.01ms`, `10.2MB`
- 최대 : `469.01ms`, `14.1MB`