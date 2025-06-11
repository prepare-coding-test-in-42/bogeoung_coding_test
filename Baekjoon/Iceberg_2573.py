from collections import deque

n, m = 0, 0
move_directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def input_func():
    global n, m

    n, m = map(int, input().split())
    ice_map = []
    for _ in range(n):
        ice_map.append(list(map(int, input().split())))

    return ice_map


def count_four_directions(ice_map, x, y):
    '''
    :param ice_map: 현재 빙산의 정보를 담고 있는 이중 리스트
    :param x: 기준이 되는 x
    :param y: 기준이 되는 y
    :return: 현재 좌표의 4방향 중 0 이하의 값의 수
    '''
    zero_count = 0
    for direction in move_directions:
        new_x, new_y = x + direction[0], y + direction[1]
        if 0 <= new_x < n and 0 <= new_y < m and ice_map[new_x][new_y] <= 0:
            zero_count += 1
    return zero_count


def spend_the_year(ice_map):
    '''
    :param ice_map: 현재 빙산의 정보를 담고 있는 이중 리스트
    :return: 주변 4방향의 빙산을 확인하고, 빙산의 높이를 동시에 낮춘 ice_map_copy 
    '''
    ice_map_copy = [row[:] for row in ice_map]
    for i in range(n):
        for j in range(m):
            if ice_map[i][j] > 0:
                ice_map_copy[i][j] = max(0, ice_map[i][j] - count_four_directions(ice_map, i, j))
    return ice_map_copy


def bfs(x, y, ice_map, visited):
    '''
    :param x: bfs의 시작점 x
    :param y: bfs의 시작점 y
    :param ice_map: 현재 빙산의 정보를 담고 있는 이중 리스트
    :param visited: 방문 여부를 담고 있는 이중 리스트
    :return: 시작점 x,y와 연결되어 있는 모든 빙산들을 방문처리하고, 반환은 없음.
    '''
    queue = deque()

    queue.append([x, y])
    while queue:
        cur_x, cur_y = queue.popleft()
        for direction in move_directions:
            new_x, new_y = cur_x + direction[0], cur_y + direction[1]
            if 0 <= new_x < n and 0 <= new_y < m and ice_map[new_x][new_y] > 0 and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                queue.append([new_x, new_y])


def count_iceberg(ice_map):
    '''
    :param ice_map: 현재 빙산의 정보를 담고 있는 이중 리스트
    :return: ice_map에서의 빙산의 개수
    '''
    visited = [[False for _ in range(m)] for _ in range(n)]
    iceberg_cnt = 0
    for i in range(n):
        for j in range(m):
            if ice_map[i][j] > 0 and not visited[i][j]:
                visited[i][j] = True
                bfs(i, j, ice_map, visited)
                iceberg_cnt += 1
    return iceberg_cnt


def run(ice_map):
    year = 0
    while True:
        year += 1
        ice_map = spend_the_year(ice_map)
        # 빙산이 2개 이상으로 나눠졌다면, 그때의 년도 반환
        if count_iceberg(ice_map) >= 2:
            return year
        
        # 만약 남아있는 얼음의 개수가 없다면 0을 반환
        total_sum = 0
        for i in range(n):
            total_sum += sum(ice_map[i])
        if total_sum <= 0:
            return 0


def main():
    ice_map = input_func()
    answer = run(ice_map)
    print(answer)


if __name__ == "__main__":
    main()
