### 문제 제목
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