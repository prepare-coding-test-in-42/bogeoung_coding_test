# BRUTEFORCE

## [최소직사각형](https://school.programmers.co.kr/learn/courses/30/lessons/86491)

#### 소요시간
- 10분

#### 간단 풀이 방식
- 한 쌍으로 입력된 값들 중 큰 값을 `width`에 저장, 작은 값을 `height`에 저장
- `max(width) * max(height)`를 반환

#### Pseudo Code
```
def solution(sizes):
    for num1, num2 in sizes:
        if num1 > num2:
            w.append(num1)
            h.append(num2)
        else:
            h.append(num1)
            w.append(num2)
            
    answer = max(w) * max(h)
    return answer
```

#### 시간복잡도
- for문 : _O(N)_
- max : _O(N)_
- 종합 : _O(N)_

#### 실행시간 및 메모리
- 최소 : `0.00ms`, `10.2MB`
- 최대 : `1.81ms`, `11.6MB`


## [모의고사](https://school.programmers.co.kr/learn/courses/30/lessons/42840)

#### 소요시간
- 10분

#### 간단 풀이 방식
- 각각의 학생별로 찍는 방식을 정리
- 모든 문제들에 대해서 학생별로 정답 여부를 확인 후 정답 개수를 저장
- 정답 개수 중 max값에 해당하는 학생들의 번호를 answer에 저장

#### Pseudo Code
```
def solution(answers):
    answerCount = [0,0,0]
    
    for index, realAnswer in enumerate(answers):
        if student1[index % 5] == realAnswer:
            answerCount[0] += 1
        if student2[index % 8] == realAnswer:
            answerCount[1] += 1
        if student3[index % 10] == realAnswer:
            answerCount[2] += 1
    
    maxNum = max(answerCount)
    for index, count in enumerate(answerCount):
        if count == maxNum:
            answer.append(index + 1)
    return answer
```

#### 시간복잡도
- 정답 확인 for 문 : _O(N)_
- max, 최대값 확인 for문 : _O(1)_
- 종합 :_O(N)_

#### 실행시간 및 메모리
- 최소 : `0.01ms`, `10.2MB`
- 최대 : `2.36ms`, `10.3MB`


## [소수 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/42839)

#### 소요시간
- 10분

#### 간단 풀이 방식
- numbers의 모든 문자들을 `numList`에 저장
- permutation 라이브러리로 `numList`의 순열값들을 계산하여 int로 변환 후 set에 저장
- set내 0,1이 존재하면 제거
- set내 모든 숫자들에 대해 소수인지 판별 후, 소수라면 answer += 1

#### Pseudo Code
```
from itertools import permutations
import math

def isPrimeNumber(number):
    if !PrimeNumber:
        return False
    
    return True

def solution(numbers): 
    for number in numbers:
        numList.append(number)
    
    permIters = set()
    for i in range(len(numList)):
        permIter = permutations(numList,i+1)
        for perm in permIter:
            permIters.add(int(''.join(perm)))
    
    permIters.remove(1)
    permIters.remove(0)
        
    for perm in permIters:
        if isPrimeNumber(perm):
            answer += 1
    return answer
```

#### 시간복잡도
- isPrimeNumber 메소드 : _O(NlogN)_
- permutations : _O(N! ⋅ √(10^N))_

#### 실행시간 및 메모리
- 최소 : `0.03ms`, `10.3MB`
- 최대 : `5.50ms`, `10.3MB`


## [카펫](https://school.programmers.co.kr/learn/courses/30/lessons/42842)

#### 소요시간
- 30분

#### 간단 풀이 방식
- 노란색으로 만들 수 있는 내부 격자의 비율을 1 부터 나눠가면서 구함
- 노란색의 w, h가 구해지면, 노란색을 둘러싸기 위한 갈색 타일의 개수와 입력 brown값을 비교

#### Pseudo Code
```
def checkEnoughBrown(canW, canH, brown):
    needBrown = ((canW + 2) * 2) + (canH * 2)
    if needBrown == brown:
        return True
    return False

def solution(brown, yellow):
    for i in range(1, yellow+1):
        if yellow % i == 0:
            if checkEnoughBrown(canW, canH, brown):
                return [canW + 2, canH + 2]

```

#### 시간복잡도
- _O(N)_

#### 실행시간 및 메모리
- 최소 : `0.00ms`, `10.1MB`
- 최대 : `0.19ms`, `10.1MB`


## [피로도](https://school.programmers.co.kr/learn/courses/30/lessons/87946)


