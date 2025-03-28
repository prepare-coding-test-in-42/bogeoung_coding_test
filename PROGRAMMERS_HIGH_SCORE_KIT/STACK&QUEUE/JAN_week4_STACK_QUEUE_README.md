# STACK / QUEUE
## 같은 숫자는 싫어
[같은 숫자는 싫어 문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12906)

#### 소요시간
- 5분

#### 간단 풀이 방식
- answer의 마지막값과 현재 arr 값을 비교함.
  - 같지 않은 값이라면 answer에 현재 값을 추가
  - 같은 값이라면 continue
  
#### Pseudo Code
```
answer = []

for num in arr:
if [num] != answer[-1:]:
    answer.append(num)
```

#### 시간복잡도
- __O(N)__

#### 실행시간 및 메모리
- 최소 : `0.00ms` , `10MB` 
- 최대 : `143.23ms`, `27.8MB`


## 기능개발
[기능개발 문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/42586)

####소요시간
- 10분

#### 간단 풀이 방식
- `progress`와 `speed`를 활용해서 필요 일수(`needDays`) 계산
- `totalNeedDays`의 마지막 값(`totalNeedDays[-1]`)과 계산된 필요 일수를 비교
  - 만약 필요 일수가 `totalNeedDays[-1]` 보다 작다면, `totalNeedDays[-1]`를 저장
  - 만약 필요 일수가 `totalNeedDays[-1]` 보다 크다면, `needDays`를 저장
  
- 배포 일수를 계산
  - `totalNeedDays[i-1]`과 `totalNeedDays[i]`가 같다면 `answer`의 마지막 값(`answer[-1]`) 에 +1
  - `totalNeedDays[i-1]`과 `totalNeedDays[i]`가 같지 않다면 `answer`에 1을 추가
  
#### Pseudo Code
```
for progress, speed in zip(progresses, speeds):
        # 필요 일수 계산
        remainDays = 100 - progress
        needDays = remainDays // speed
        if (remainDays % speed) != 0:
            needDays += 1
        
        # 선행 배포가 완료되었는지 확인
        if(totalNeedDays and (totalNeedDays[-1] > needDays)):
            totalNeedDays.append(totalNeedDays[-1])
        else:
            totalNeedDays.append(needDays)
    
    for idx in range(1, len(totalNeedDays)):
        if totalNeedDays[idx] == totalNeedDays[idx -1]:
            answer[-1] += 1
        else:
            answer.append(1)
```

#### 시간복잡도
- 필요 일수 계산 : __O(N)__
- 배포 일자 계산 : __O(N)__

#### 실행시간 및 메모리
- 최소 : `0.01ms`, `10.1MB`
- 최대 : `0.07ms`, `10.2MB`

## 올바른 괄호
[올바른 괄호 문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12909)

#### 소요시간
- 10분

#### 간단 풀이 방식
- "("가 들어오는 경우에는 stack에 add
- ")"가 들어오는 경우에는 아래 두가지 행동 중 하나를 수행
  - stack에 값이 존재하지 않다면 `False` 리턴
  - stack에 값이 존재한다면 `stack.pop()` 수행 
- 입력된 S에 대해서 모두 수행한 후 stack에 값이 남아있다면 `False` 리턴

#### Pseudo Code
```
def solution(s):
    stack = []
    
    for bracket in s:
        if bracket == "(":
            stack.append()
        if bracket == ")" and len(stack) == 0:
            return False
        if bracket == ")" and len(stack) > 0:
            stack.pop()
    
    if len(stack) > 0:
        return False
    
    return True
```

#### 시간복잡도
- _O(N)_

#### 실행시간 및 메모리
- 최소 : `0.00ms`, `10.1MB`
- 최대 : `16.39ms`, `10.4MB`

## 프로세스
[프로세스 문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/42587)

#### 소요시간
- 25분

#### 간단 풀이 방식
- 같은 우선순위가 존재하는 상황에서 location에 위치한 프로세스를 어떻게 특정할지가 고민이였음.
- 반복문을 수행하면서 location의 값 또한 변화시켜서 해결.

1. 우선순위 리스트의 상단의 값을 pop(`curPriority`)
2. `curPriority`가 우선순위 리스트 내의 가장 우선순위가 높은 값이라면
   - 현재까지 실행된 프로세스의 수(`curProcessOrder`)를 1 증가시킴
   - `loctaion`의 값이 0이라면, `curProcessOrder`를 리턴
   - `location`의 값이 0 이상이라면, `location` 값을 1 감소
3.`curPriority`가 우선순위 리스트 내의 가장 우선순위가 높은 값이 아니라면
   - 우선순위 리스트에 `curPriority`를 append
   - `location`의 값이 0이라면, 현재 우선순위 리스트의 길이로 업데이트
   - `location`의 값이 0 이상이라면, `location` 값을 1 감소

#### Pseudo Code
```
'''
location에 위치하는 프로세스를 어떻게 특정할지가 고민이네.
같은 우선순위가 있기 때문에 우선순위로 식별할수가 없음.
location의 위치를 계속해서 변경해나가야 하나?
'''
def solution(priorities, location):
    curProcessOrder = 0
    
    while(True):
        maxPriority = max(priorities)
        curPriority = priorities.pop(0)
        # 우선순위가 제일 높은 프로세스라면
        if curPriority == maxPriority:
            curProcessOrder += 1
            # 찾으려던 프로세스인 경우
                return curProcessOrder
            # 그렇지 않은 경우
                location -= 1
        # 우선순위가 제일 높지 않다면 제일 후순위로 미룸
        if curPriority != maxPriority:
            priorities.append(curPriority)
            # 찾으려던 프로세스인 경우
                location = len(priorities) 
            # 그렇지 않은 경우
                location -= 1
        
    return curProcessOrder
```

#### 시간복잡도
- _O(N)_

#### 실행시간 및 메모리
- 최소 : `0.01ms`, `10.1MB`
- 최대 : `0.69ms`, `10.4MB`

## 다리를 지나는 트럭
- 30분 -> case 4,5,6,9 실패
- 30분 + 1시간 -> case 11 실패
- 
#### 소요시간

#### 간단 풀이 방식

#### Pseudo Code
```

```

#### 시간복잡도

#### 실행시간 및 메모리
- 최소 : 
- 최대 : 

## 주식 가격

#### 소요시간
- 10분

#### 간단 풀이 방식
- 현재 시점 이후의 모든 값들을 비교
- 값이 작아지는 순간이 있으면 현재시점 - 작아지는 순간을 answer에 append
- 작아지는 순간이 없으면 len(prices) - 현재 시점의 값을 answer에 append

#### Pseudo Code
```
def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        flag = False
        for j in range(i, len(prices)):
            if prices[j] < prices[i]:
                answer.append(j-i)
                flag=True
                break
        if flag == False:
            answer.append(len(prices) - i - 1)
            
    return answer
```

#### 시간복잡도
- _O(N^2)_

#### 실행시간 및 메모리
- 최소 : `0.01ms`, `9.99MB`
- 최대 : `129.64ms`, `19.4MB`

## 다리를 지나는 트럭
[다리를 지나는 트럭 문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/42583)

#### 소요시간
- 하루 종일 + 팀원 피드백

#### 간단 풀이 방식
- 다리에 올라간 트럭들의 무게를 관리하는 리스트 `curBridgeWeight`
- 다리에 올라간 트럭들의 남은 이동거리를 관리하는 리스트 `curBridgeLength`
- curBridgeWeight의 합이 weight를 넘지 않으면서, len(curBridgeLength)이 다리길이를 넘지 않는 동안 아래 반복문 수행
  - 다리에 트럭을 추가할 수 없는 경우
    - 다리에 새로운 트럭을 넣을 수 있을때까지 먼저 들어온 순으로 트럭을 제거
    - 제거된 트럭의 남은 길이는 answer에 추가
  - 다리에 트럭을 추가할 수 있는 경우
    - 다리에 트럭을 추가
    - 현재 다리 위에 존재하는 트럭들의 남은 이동거리 -1
  - 다리 위에 트럭이 남은 경우 남은 이동거리 만큼 answer에 추가

#### Pseudo Code
```
'''
- 일차선 다리를 정해진 순으로
- 모든 트럭이 다리를 건너려면 최소 몇초가 걸리는지?
- 다리에는 트럭이 최대 bridge_length대 
- 다리는 weight 이하의 무게까지 견딜 수 있음.(다리에 완전히 오르지 않은 트럭의 무게는 무시)
- 다리를 건너는데 걸리는 시간은 bridge_lenght

'''

def updateBridge(bridge, num):
    # bridge 내에 존재하는 모든 트럭의 남은 이동거리를 num 만큼 감소

def solution(bridge_length, weight, truck_weights):
    for truck in truck_weights:
        # 다리에 트럭이 추가가 불가능한 경우
        if sum(curBridgeWeight) + truck > weight:
            while(sum(curBridgeWeight) > weight - truck):
                # 가장 먼저 들어간 트럭부터 모두 지나도록 계산
                frontOfBridgeLength = curBridgeLength.pop(0)
                answer += frontOfBridgeLength 
                curBridgeLength = updateBridge(curBridgeLength, frontOfBridgeLength)
    
        # 다리에 트럭이 추가될 수 있는 경우
        if sum(curBridgeWeight) + truck <= weight and len(curBridgeWeight) < bridge_length:
            curBridgeWeight.append(truck)
            curBridgeLength.append(bridge_length)
            answer += 1
            
            # 한 칸씩 이동
            curBridgeLength = updateBridge(curBridgeLength,1)
            # 다리를 다 건넌 트럭이 존재하는 경우
            if curBridgeLength and curBridgeLength[0] == 0:
                curBridgeLength.pop(0)
                curBridgeWeight.pop(0)
    
    if(len(curBridgeLength) != 0):
        answer += curBridgeLength[-1]
    return answer
```
#### 시간복잡도
- for 문 : _O(N)_
- for문 내부 : _O(N)_
- 종합 : _O(N^2)_

#### 실행시간 및 메모리
- 최소 : `0.01ms`, `10.2MB`
- 최대 : `4.11ms`, `10.3MB`