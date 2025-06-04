## [이차원 배열과 연산](https://www.acmicpc.net/problem/17140)

#### 소요시간
- 1시간 30분

#### 간단 풀이 방식
- 간단 풀이 방식을 작성합니다.

#### Pseudo Code
```
def r_operation(input_array):
    max_row = 0
    new_input_array = []
    for row in input_array:
        count = Counter(x for x in row if x != 0)
        sorted_count = sorted(count.items(), key = lambda x : [x[1], x[0]])
        
        new_row = []
        for num, count in sorted_count:
            new_row.extend([num, count])
        max_row = max(max_row, len(new_row))
        new_input_array.append(new_row)

    for row in new_input_array:
        row.extend([0] * (max_row - len(row)))
        if len(row) > 100:
            row = row[:100]
    return new_input_array
```

#### 시간복잡도
- `r_operation`, `c_operation` : $O(R \cdot M log M)$ 
  * R은 현재 행 혹은 열의 수
- 종합 : $O(T \cdot R \cdot M log M)$ 
  * T는 연산 횟수, R은 현재 배열의 행 또는 열의 수, M은 각 행 또는 열의 길이

#### 소요시간 및 메모리
- 메모리 : 35068 KB
- 소요시간 : 72 ms

