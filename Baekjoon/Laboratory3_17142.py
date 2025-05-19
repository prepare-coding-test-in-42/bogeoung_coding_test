import copy
from itertools import combinations
from collections import deque

VIRUS = 2
n = 0
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def input_func():
    global n
    n, m = map(int, input().split())

    lab_map = []
    for _ in range(n):
        lab_map.append(list(map(int, input().split())))

    return m, lab_map


def find_num_in_map(lab_map, find_num):
    locations = []

    for i in range(n):
        for j in range(n):
            if lab_map[i][j] == find_num:
                locations.append([i, j])
    return locations


def init_copy_map(comb, lab_map):
    # 활성화 시킬 바이러스 제외 비활성화
    copy_lab_map = copy.deepcopy(lab_map)

    for i in range(n):
        for j in range(n):
            if lab_map[i][j] == 0:
                copy_lab_map[i][j] = -1
            elif lab_map[i][j] == 1:
                copy_lab_map[i][j] = '-'
            elif lab_map[i][j] == 2:
                if [i, j] not in comb:
                    copy_lab_map[i][j] = '*'
                else:
                    copy_lab_map[i][j] = 0

    return copy_lab_map


def spread_virus(lab_map, remain_count):
    queue = deque()

    for x, y in find_num_in_map(lab_map, 0):
        queue.append([x, y, 0])

    while queue:
        x, y, time = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if lab_map[nx][ny] in [-1, '*']:
                    if lab_map[nx][ny] == -1:
                        remain_count -= 1
                    lab_map[nx][ny] = time + 1
                    queue.append([nx, ny, time + 1])

                if remain_count <= 0:
                    return time + 1
    if remain_count > 0:
        return -1

    return 0


def main():
    m, lab_map = input_func()
    answer = 1e9
    virus_locations = find_num_in_map(lab_map, VIRUS)
    combs = combinations(virus_locations, m)

    for comb in combs:
        copied_map = init_copy_map(comb, lab_map)
        remain_count = len(find_num_in_map(lab_map, 0))
        if remain_count == 0:
            print(0)
            return
        else:
            spent_time = spread_virus(copied_map, remain_count)
            if spent_time > 0:
                answer = min(answer, spent_time)

    if answer == 1e9:
        print(-1)
        return
    print(answer)


if __name__ == "__main__":
    main()
