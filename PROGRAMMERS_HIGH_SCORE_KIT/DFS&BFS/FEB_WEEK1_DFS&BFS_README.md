## [타겟 넘버](https://school.programmers.co.kr/learn/courses/30/lessons/43165)

#### 소요시간
- 10분

#### 간단 풀이 방식
- DFS를 활용해서 가능한 모든 조합을 검색
- 마지막 인덱스까지 돌았을때의 합이 타겟넘버와 같다면 answer += 1

#### Pseudo Code
```

```

#### 시간복잡도

#### 실행시간 및 메모리
- 최소 : `0.46ms`, `10.2MB`
- 최대 : `471.94ms`, `10.1MB`


## [네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162)

#### 소요시간
- 10분

#### 간단 풀이 방식
- BFS를 활용해서 start node부터 연결된 모든 컴퓨터를 방문 후 네트워크의 수를 나타내는 answer += 1
- 방문한 컴퓨터는 visited로 관리
- 모든 컴퓨터에 방문했을 때의 answer 값을 리턴

#### Pseudo Code
```

```

#### 시간복잡도

#### 실행시간 및 메모리
- 최소 : `0.01ms`, `10.1MB`
- 최대 : `6.55ms`, `10.1MB`

## [게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844)

#### 소요시간
- 약 45분 (정확성은 15분만에 해결했으나 효율성에서 고생함..)

#### 간단 풀이 방식

#### Pseudo Code
```

```

#### 시간복잡도

#### 실행시간 및 메모리
- 최소 : `0.01ms`, `10.1MB`
- 최대 : `14.03ms`, `10.1MB`

## [단어 변환](https://school.programmers.co.kr/learn/courses/30/lessons/43163)

#### 소요시간
- 약 25분
- 아래 탈출 조건에서 시간 소요가 많이 됨
```
    if len(words) + 1 <= len(visited) and cur_word != target:
        answer = min(answer, len(visited))
        return 
```
처음 위 조건을 선언했을 당시 모든 단어로 변환을 했지만 target 단어로 변환에 실패했을 때 0을 리턴하는 것으로 생각  
하지만 모든 단어로 변환을 못할 수 있음을 고려 못함(문자 차이가 2개 이상이여서 사용 못하는 단어가 존재할 수 있음).  
위와 같은 상황이라면 `len(words) + 1 <= len(visited)`가 성립이 안되면서 조건문에 진입하지 못해 오답이 발생

#### 간단 풀이 방식
- `count_diff_word` : word1과 word2간의 문자 차이를 세는 메소드
- `dfs` : 사용하지 않은 단어 중 현재 단어와 글자수의 차이가 1개인 단어로 변환
- 
#### Pseudo Code
````

````

#### 실행시간 및 메모리
- 최소 : `0.00ms`, `10.2MB`
- 최대 : `0.36ms`, `10.2MB`

## [여행 경로](https://school.programmers.co.kr/learn/courses/30/lessons/43164)

#### 소요시간
- 약 30분
- 처음에 사용한 티켓들을 tickets에서 제거해가면서 풀었는데 런타임에러가 발생하였음.
- 런타임 에러의 이유를 찾는데 많은 시간이 소요됐으며, 결국 챗지피티의 도움을 받음.
- 사용한 티켓들을 제거하지 않고, 사용 여부를 저장하는 방향으로 수정하여 해결

#### 간단 풀이 방식
- `dfs` : 현재 티켓의 도착지가 새티켓의 출발지이면서, 이전에 사용하지 않은 티켓이라면 해당 티켓을 사용
- "ICN"에서 출발하는 티켓들에 대해서 dfs 수행
- 모든 티켓을 다 소진했을 때의 경로를 answer에 append
- answer를 정렬해서 가장 처음에 나온 요소를 리턴

#### Pseudo Code
```

```

#### 시간복잡도

#### 실행시간 및 메모리
- 최소 : `0.01ms`, `10.2MB`
- 최대 : `355.15ms`, `14.5MB`