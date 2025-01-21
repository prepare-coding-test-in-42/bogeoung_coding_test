# HEAP
## 더 맵게

#### 소요시간
- 15분

#### 간단 풀이 방식
- heapq 라이브러리를 활용
- 가장 처음 원소의 값이 K보다 클때까지 아래 행동을 반복
  - 0번째와 1번째의 원소로 새 음식을 만들어 heap에 push
  - 만약 heap의 길이가 1이하일 경우 -1 리턴

#### Pseudo Code
```
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        if scoville[0] >= K:
            break
        if(len(scoville) <= 1):
            return -1
        newFood = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, newFood)
        answer += 1
    return answer
```

#### 시간복잡도
- Heapq.heapify : _O (N)_
- heapq.heappop : _O (logN)_
- heapq.heappush : _O (logN)_
- 최종 : _O (N log N)_

#### 실행시간 및 메모리
- 최소 : `0.00ms`, `9.95MB`
- 최대 : `1904.67ms`, `49.6MB`

## 디스크 컨트롤러

#### 소요시간
- 1시간 30분

#### 간단 풀이 방식

#### Pseudo Code
```
import heapq

def addJobs(jobs, heapJobs, curTime):
    # curTime 기준으로 현재 시점 이전에 들어온 Jobs들을 heapJobs에 추가
    # jobs를 업데이트 
    return jobs


def scheduling(heapJobs, curTime, answer, jobs):
    while heapJobs:
        # 가장 소요시간이 적은 것부터 추출하여 answer와 curTime 업데이트
        # jobs 업데이트
        jobs = addJobs(jobs, heapJobs, curTime)

    return [curTime, answer, jobs]


def solution(jobs):
    answer = 0
    lenJobs = len(jobs)
    heapJobs = []
    heapq.heapify(heapJobs)
    curTime = 0
    
    jobs.sort(key=lambda x: [x[0], x[1]])
    while jobs:
        firstJob = jobs.pop(0)
        heapq.heappush(heapJobs, (firstJob[1], firstJob[0]))
        curTime, answer, jobs = scheduling(heapJobs, curTime, answer, jobs)

    return answer // lenJobs
```

#### 시간복잡도
- list.sort : _O (N log N)_
- addJobs 함수 : _O (N)_
- scheduling 함수의 heappop, heappush : _O (log M)_
- 최종 : _O (N^2)_

#### 실행시간 및 메모리
- 최소 : `0.01ms`, `10.2MB`
- 최대 : `1.02ms`, `10.3MB`