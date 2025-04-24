## [기타콘서트](https://www.acmicpc.net/problem/1497)

#### 소요시간
- 30분 내

#### 간단 풀이 방식
- `itertools`의 `combinations`를 활용하여 가능한 모든 기타의 조합에 대해서 연주 가능한 곡의 수를 계산
- 연주 가능한 곡의 수가 모든 곡의 수가 같다면 그때의 기타의 수를 반환
- 만약 연주가 가능한 곡의 수가 없다면 -1을 반환
- 만약 일부 곡을 연주할 수가 없다면 연주 가능한 곡이 최대일때의 기타의 수를 반환

#### Pseudo Code
```
def run(n, m, guitar_infos):
    max_comb_results_guitar_count = 0
    max_comb_results = 0
    for i in range(1, n+1):
        combs = combinations(guitar_infos, i)
        for comb in combs:
            available_songs = count_available_songs(m, comb)
            if available_songs == m:
                return i
            elif available_songs > max_comb_results:
                max_comb_results = available_songs
                max_comb_results_guitar_count = i
```

#### 시간복잡도
- 총 조합의 수 : $2^n -1$
- `count_available_songs` : $O(m \cdot k)
- 종합 : $O(2^n -1 \cdot m \cdot \k)

#### 소요시간 및 메모리
- 메모리 : 32412 KB
- 소요시간 : 48 ms

## [물약 구매](https://www.acmicpc.net/problem/24954)

#### 소요시간
- 30분

#### 간단 풀이 방식
- `itertools`의 `permutations`를 활용하여 가능한 물약의 순열을 모두 구한다.
- 각 순열에 대해서 순서대로 물약을 사면서, 할인 이벤트가 존재한다면 물약 가격을 업데이트하며, 구매 가격을 계산한다.
- pypy로만 통과하고 python으로 풀이하는 경우 시간 초과가 남. -> 비트마스크를 활용하면 된다는데 찾아봐야할듯.

#### Pseudo Code
```
def run(potion_prices, discount_prices):
    answer = 1000000
    potion_indices = [int(i) for i in range(len(potion_prices))]
    perms = permutations(potion_indices, len(potion_prices))

    for perm in perms:
        current_prices = 0
        current_potion_prices = potion_prices[:]
        for potion_index in perm:
            current_prices += current_potion_prices[potion_index]
            if discount_prices[potion_index]:
                current_potion_prices = potion_prices_update(current_potion_prices, discount_prices[potion_index])

        answer = min(answer, current_prices)
    return answer
```

#### 시간복잡도
- `permutations` : $O(n!)$
- `potion_prices_update` : $O(n)$
- 종합 : $O(n! \cdot n)$

#### 소요시간 및 메모리 (**PyPy3 기준**)
- 메모리 : 114252 KB
- 소요시간 : 3588 ms

## [치킨 배달](https://www.acmicpc.net/problem/15686)

#### 소요시간
- 약 30분

#### 간단 풀이 방식
- `itertools`의 `combinations`를 활용하여 가능한 모든 케이스를 탐색하고, 답을 갱신

#### Pseudo Code
```
def run(n, m, city_map):
    answer = 99999
    chicken_locs = find_specific_loc(n, city_map, 2)
    house_locs = find_specific_loc(n, city_map, 1)
    combs = combinations(chicken_locs, m)
    for comb in combs:
        answer = min(answer,find_city_chicken_distance(comb, house_locs))
    return answer
```

#### 시간복잡도
- $O(n^2)$

#### 소요시간 및 메모리 
- 메모리 : 32412 KB
- 소요시간 : 188 ms

## [인구 이동](https://www.acmicpc.net/problem/16234)

#### 소요시간
- 30분

#### 간단 풀이 방식
- BFS를 활용하여 인접한 국가들을 연합으로 묶어 풀이

#### Pseudo Code
```
def run(n, l, r, population_map):
    move_flag = True
    answer = 0
    while move_flag:
        move_flag = False
        visited = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    visited[i][j] = True
                    unions = make_union(i, j, n, l, r, visited, population_map)
                    if len(unions) > 1:
                        move_flag = True
                        update_unions(unions, population_map)
        if move_flag:
            answer += 1
        else:
            move_flag = False
    return answer
```

#### 시간복잡도
- `run` : $O(n^2)$
- `make_union` : $O(n^2)$
- `update_union` : 최악의 경우$O(n^2)$
- 종합 : $O(n^4)$

#### 소요시간 및 메모리
- 메모리 : 33432 KB
- 소요시간 : 4600 ms

## [마법사 상어와 비바라기](https://www.acmicpc.net/problem/21610)

#### 소요시간
- 2시간 이상

#### 간단 풀이 방식
- 문제 그대로 구현.

헤맸던 부분
1. 구름을 좌표 하나마다 만들지 않고, 하나의 덩어리로 취급 & while문으로 처리
   - 초반 구름의 좌표가 4개로 고정되어 있어서, 4개의 좌표를 하나로 묶어 하나의 구름으로 만들었었음.
   - 이후 매 단계에서 1개의 구름을 만들되, 여러 좌표를 가지도록 하였음. 
   - 한 구름에 여러 좌표들을 가지고 있기에 while문을 활용하여 구름 이동, 비내리기 등을 수행
   - 이 과정에서 pop을 활용하게 되었지만, 해당 좌표 값을 물복사버그 마법 시전시 필요했기 때문에 다시 저장하는 과정이 발생 
   - 복잡할 뿐만 아니라 비효율적이라 생각하여 초반 구름을 4개(좌표 별로 1개씩)로 만들어서 해결
2. direction 좌표를 업데이트 하는 과정
   - 좌표가 map의 크기를 2번 이상 넘어간다는 것을 고려하지 못해 헤맸음.

#### Pseudo Code
```
def run(n, ground_map, move_methods):
    clouds = []
    init_locations = [[n - 2, 0], [n - 2, 1], [n - 1, 0], [n - 1, 1]]
    for location in init_locations:
        clouds.append(Cloud(n, location))

    for move_direction, move_number in move_methods:
        disappeared_cloud_locations = []
        for cloud in clouds:
            cloud.move(move_direction, move_number)
            cloud.rain(ground_map)
            disappeared_cloud_locations.append([cloud.x, cloud.y])

        clouds = []
        for d_cloud in disappeared_cloud_locations:
            update_location_with_bug(n, ground_map, d_cloud[0], d_cloud[1])
        new_clouds_locations = make_new_clouds(ground_map, disappeared_cloud_locations)
        for locations in new_clouds_locations:
            clouds.append(Cloud(n, locations))

    answer = 0
    for row in ground_map:
        answer += sum(row)

    return answer
```

#### 시간복잡도
- $O(m \cdot n^2)$

#### 소요시간 및 메모리
- 메모리 : 33432 KB
- 소요시간 : 272ms
