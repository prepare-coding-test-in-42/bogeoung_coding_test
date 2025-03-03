# BINARYSEARCH
## [숫자 게임](https://school.programmers.co.kr/learn/courses/30/lessons/12987)

#### 소요시간
- 20분

#### 간단 풀이 방식
- 배열 `B` 정렬
- 배열 `A`의 각 숫자에 대해 아래 과정을 수행
  - `find_winning_numbers` : `A`의 각 숫자에 대해, 배열 `B`에서 해당 숫자보다 크면서 가장 작은 숫자의 index를 찾음
  - `find_winning_numbers`의 반환값이 유효하다면 `answer += 1`, 해당 숫자를 `B`에서 제거
 
- (다 풀고나서 다른 분의 풀이를 보는데 `A`와 `B` 둘다 정렬하고, `B`의 값을 순회하면서 `A`보다 큰 숫자가 있으면, 해당 숫자를 제거하면 되는 거였음.. )
#### Pseudo Code
```
function solution(A, B):
    answer = 0
    sort array B

    for each number in array A:
        min_winning_index = find_winning_numbers(B, number)
        
        # If a winning number is found, increment answer and remove the number from B
        if min_winning_index > 0 or (min_winning_index == 0 and number < B[0]):
            increment answer by 1
            remove B[min_winning_index]

    return answer

function find_winning_numbers(B, A_num):
    left = 0
    right = length of B - 1
    min_winning_index = 0

    while left <= right:
        mid = (left + right) // 2

        if B[mid] > A_num:
            min_winning_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return min_winning_index

```

#### 시간복잡도
- 정렬 : __O(N log N)__
- find_winning_numbers : __O(M log N)__
- 숫자 제거 : __O(M * N)__  
  * 이진 탐색 알고리즘의 시간복잡도는 O(log N)이고, 숫자 제거의 시간복잡도는 O(N)이지만, 배열 A의 크기`M`만큼 수행 하기 때문

- 종합 : __O(N^2)__
  * 배열 `A`와 `B`의 크기는 항상 같기 때문
  
#### 실행시간 및 메모리
- 최소 : `0.01ms`, `10.1MB`
- 최대 : `546.14ms`, `18.6MB`