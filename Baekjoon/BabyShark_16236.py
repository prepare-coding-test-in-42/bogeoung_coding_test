import sys
from collections import deque


def input_func():
    n = int(input())
    sea_map = [list(map(int, input().split())) for _ in range(n)]
    return n, sea_map

class Shark:
    def __init__(self, x, y, age=2):
        self.x = x
        self.y = y
        self.age = age
        self.remain_to_grow = 2

    def eat(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.remain_to_grow -= 1
        if self.remain_to_grow == 0:
            self.age += 1
            self.remain_to_grow = self.age

def bfs(n, sea_map, shark):
    visited = [[-1] * n for _ in range(n)]
    queue = deque()
    queue.append((shark.x, shark.y))
    visited[shark.x][shark.y] = 0

    fish_list = []
    min_dist = sys.maxsize
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # 위 -> 왼 -> 오 -> 아래 우선순위

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n:
                # 방문하지 않았고, 상어 크기 이하로 이동 가능
                if visited[nx][ny] == -1 and sea_map[nx][ny] <= shark.age:
                    visited[nx][ny] = visited[x][y] + 1
                    # 먹을 수 있는 물고기 발견
                    if 0 < sea_map[nx][ny] < shark.age:
                        distance = visited[nx][ny]
                        if distance < min_dist:
                            fish_list = [(nx, ny, distance)]
                            min_dist = distance
                        elif distance == min_dist:
                            fish_list.append((nx, ny, distance))
                    else:
                        queue.append((nx, ny))

    if fish_list:
        fish_list.sort()  # 가장 위, 왼쪽 우선
        return fish_list[0]  # (x, y, 거리)
    else:
        return None

def run(n, sea_map):
    # 아기 상어 찾기
    for i in range(n):
        for j in range(n):
            if sea_map[i][j] == 9:
                baby_shark = Shark(i, j)
                sea_map[i][j] = 0  # 시작 위치 비우기
                break

    total_time = 0

    while True:
        result = bfs(n, sea_map, baby_shark)
        if result is None:
            return total_time

        eat_x, eat_y, distance = result
        baby_shark.eat(eat_x, eat_y)
        sea_map[eat_x][eat_y] = 0
        total_time += distance

def main():
    n, sea_map = input_func()
    print(run(n, sea_map))

if __name__ == "__main__":
    main()
