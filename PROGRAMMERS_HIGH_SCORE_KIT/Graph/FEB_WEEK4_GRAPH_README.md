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