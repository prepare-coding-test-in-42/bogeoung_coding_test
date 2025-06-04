# GRAPH
## [가장 먼 노드](https://school.programmers.co.kr/learn/courses/30/lessons/49189)

#### 소요시간
- 15분

#### 간단 풀이 방식
- 매개변수 `edge`로부터 간선 정보를 뽑아 `edge_map`에 저장
- 1번 노드서부터 연결된 노드들을 순회하며, 1번으로부터 떨어져있는 거리를 `length_from_one` 저장
- `length_from_one`에서의 `max`값을 계산하고, max값과 같은 개수를 반환

#### Pseudo Code
```
Function find_distance(edge_map):
    Initialize a queue to store (node, distance) pairs (start from node 1, distance 0)
    Initialize a list to track visited nodes
    Initialize a list to store distances from node 1

    While queue is not empty:
        remove and retrieve the first element from the queue

        If the node has not been visited
            Mark the node as visited
            Store the distance

            For each connected_node in edge_map[cur_node]:
                Add connected node and incremented distance to the queue

    Return list for distances
    
Function solution(n, edge):
    answer = 0

    Initialize the graph
    Store the edge information in edge_map (bidirectional)

    Calculate the distance from node 1 to each node

    Find the farthest distance
    Count the number of nodes at the farthest distance
    Return the result

```

#### 시간복잡도
- edge_map 초기화 : __O(N)__
- edge 정보 저장 : __O(E)__  
   * E : edge의 크기 
- 최대 거리 찾기 : __O(N)__
- 종합 : __O(N + E)__

#### 실행시간 및 메모리
- 최소 : `0.02ms`, `10.2MB`
- 최대 : `612.23ms`, `24.4MB`

## [순위](https://school.programmers.co.kr/learn/courses/30/lessons/49191)

#### 소요시간
- 1시간 이상 + 검색

#### 간단 풀이 방식
- 승패 정보를 `map`에 저장.
- 플로이드-워셜 알고리즘을 활용하여 승패 정보를 업데이트  
ex) 1번 선수가 2번 선수를 이기고, 2번 선수가 3번 선수를 이김 -> 1번 선수가 3번을 이겼다고 업데이트
- 각 선수별로 승패 여부를 알 수 없는 번호가 2개라면(0과 자기자신) 모든 선수와의 승패여부를 알 수 있으므로 `answer += 1`

#### Pseudo Code
```
function solution(n, results):
    create 2D array map of size (n+1) x (n+1) filled with 0

    for each (winner, loser) in results:
        map[winner][loser] = 1  
        map[loser][winner] = -1  

    for k from 1 to n:
        for i from 1 to n:
            for j from 1 to n:
                if i == j:
                    continue
                if map[i][k] == 1 and map[k][j] == 1:
                    map[i][j] = 1
                    map[j][i] = -1
                    map[j][k] = -1
                    map[k][i] = -1

    count = 0
    for each row in map:
        if count of 0 in row == 2:
            count += 1

    return count
```

#### 시간복잡도
- 플로이드-워셜 알고리즘 : __O(N^3)__
- 순위 확정 여부 계산 : __O(N^2)__
- 종합 : __O(N^3)__

#### 실행시간 및 메모리
- 최소 : `0.03ms`, `10.1MB`
- 최대 : `166.35ms`, `10.6MB`