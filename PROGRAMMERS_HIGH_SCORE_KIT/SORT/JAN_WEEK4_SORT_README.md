# 정렬

## K번째수
[K번째수 문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/42748)

#### 소요시간
- 5분

#### 간단 풀이 방식
- i번째부터 j번째까지 리스트 슬라이싱 수행
- 슬라이싱 한 리스트를 정렬시킨 후 k번째 원소 리턴
  
#### Pseudo Code
```
def solution(array, commands):
    answer = []
    
    for i,j,k in commands:
        newArray = array[i-1 : j]
        newArray.sort()
        answer.append(newArray[k-1])
    return answer
```

#### 시간복잡도
- 리스트 슬라이싱 : _O(N)_ 
*N은 슬라이싱 한 범위의 길이
- 정렬 : _O(N logN)_
-  값 추출 : _O(1)_
- 종합 : _O(M ⋅ N logN)_

#### 실행시간 및 메모리
- 최소 : `0.00ms` , `10.1MB` 
- 최대 :  `0.00ms` , `10.4MB` 

## 가장 큰 수
[가장 큰 수 문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/42746)

#### 소요시간
- 못풀어서 결국 구글링

#### 간단 풀이 방식
- 구글링
  
#### Pseudo Code
```
def solution(numbers):
    num = list(map(str, numbers))
    num.sort(key = lambda x :x*3, reverse = True)
    return str(int(''.join(num)))
```

#### 시간복잡도
- map : _O(N)_
- 정렬 : _O(k ⋅ N logN)_
*K는 각 문자열의 길이
- join : _O(L)_
*L은 리스트에 포함된 길이의 합, N ⋅ K와 거의 유사
*정수형 변환 : _O(L)_
- 종합 : _O(N ⋅ log N)_

#### 실행시간 및 메모리
- 최소 : `0.02ms`, `10.2MB`
- 최대 : `1445.18ms`, `26.9MB`

### H-Index
#### 소요 시간
- 1시간 
- 간단히 풀 수 있는 로직을 어렵게 생각하여 생각보다 시간이 소요되었습니다.

#### 간단 풀이 방식
- 논문 인용 횟수가 담긴 배열 citations을 오름차순으로 정렬
- citations의 max값 + 1 까지 for문을 반복
  - getMaxIndexOfInputNumber 메소드를 활용하여 현재 h값보다 큰 값의 개수를 계산
  - 큰 값의 개수가 h보다 큰 경우 answer에 저장
- answer를 리턴

#### Pseudo Code
````
def getMaxIndexOfInputNumber(number, citations):
    for i in range(len(citations)):
        ...
        if(citations[i] >= number):
            index = i;
            break
    return index;
    
def solution(citations):
    answer = 0
    citations.sort()
    for h in range(citations[-1] + 1):
        numberOfMoreThanH = len(citations) - getMaxIndexOfInputNumber(h, citations)
        if(numberOfMoreThanH >= h):
            answer = h
            
    return answer
````

### 메모리 및 시간
- 최대 : 304.76ms, 10.3mb
- 최소 : 0.0ms, 10.3mb