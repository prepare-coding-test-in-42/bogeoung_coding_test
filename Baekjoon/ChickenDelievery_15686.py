"""
1. n * n 도시, 도시의 각 칸은 빈칸(0), 치킨집(2), 집(1) 중 하나
2. 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리
3. 각각의 집은 치킨 거리를 가지며, 도시의 치킨 거리는 모든 집의 치킨 거리의 합
4. 치킨집을 m개를 제외하고 모두 폐업시켰을 때, 도시의 치킨 거리를 가장 작게 하는 프로그램
"""
from itertools import combinations

def input_func():
    n, m = map(int, input().split())

    city_map = []
    for _ in range(n):
        city_map.append(list(map(int, input().split())))

    return n,m, city_map


def find_specific_loc(n,city_map,find_num):
    find_locs = []
    for i in range(n):
        for j in range(n):
            if city_map[i][j] == find_num:
                find_locs.append([i,j])
    return find_locs


def find_city_chicken_distance(chicken_locs, house_locs):
    city_chicken_distance = 0
    for house_x, house_y in house_locs:
        minimum_chicken_distance = 99999
        for chicken_x, chicken_y in chicken_locs:
            minimum_chicken_distance = min(minimum_chicken_distance, abs(house_x - chicken_x) + abs(house_y - chicken_y))
        city_chicken_distance += minimum_chicken_distance
    return city_chicken_distance


def run(n, m, city_map):
    answer = 99999
    chicken_locs = find_specific_loc(n, city_map, 2)
    house_locs = find_specific_loc(n, city_map, 1)
    combs = combinations(chicken_locs, m)
    for comb in combs:
        answer = min(answer,find_city_chicken_distance(comb, house_locs))
    return answer

def main():
    n,m,city_map = input_func()
    answer = run(n,m,city_map)
    print(answer)

if __name__ == "__main__":
    main()