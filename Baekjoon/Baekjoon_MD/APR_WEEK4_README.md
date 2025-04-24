## [나무 재테크](https://www.acmicpc.net/problem/16235)

#### 소요시간
- 

#### 간단 풀이 방식
- 

#### Pseudo Code
```

```

#### 시간복잡도
- 

#### 소요시간 및 메모리
- 메모리 :  KB
- 소요시간 : ms

## [컨베이어 벨트위의 로봇](https://www.acmicpc.net/problem/20055)

#### 소요시간
- 30분

#### 간단 풀이 방식
- 문제 대로 구현.
- 문제에서 방햐잉 바뀌는 부분이 존재하였지만, 파이썬의 리스트를 활용하여 단순하게 구현.
- 다만 문제를 제대로 읽지 않아 n번째에서 기계를 내린다는 것을 2n위치에서 내린다고 헤맸음.

#### Pseudo Code
```
def run(n, k, durability):
    answer = 1
    convey_belt = [0 for _ in range(2 * n)]
    while True:
        durability = rotate(durability)
        convey_belt = rotate(convey_belt)
        flag, convey_belt, durability = move_robot(n,convey_belt, durability)
        if not flag:
            return answer

        if convey_belt[n -1] == 1:
            convey_belt[n-1] = 0
        if convey_belt[0] == 0 and durability[0] >= 1:
            convey_belt[0] += 1
            durability[0] -= 1

        if durability.count(0) >= k:
            return answer
        answer += 1

```

#### 시간복잡도
- $O(n\cdot k)$ *k는 while에서 반복되는 `rotate`, `move_robot`, `durability.count(0)` 메소드들의 실행횟수 

#### 소요시간 및 메모리 
- 메모리 : 32412 KB
- 소요시간 : 3224 ms
