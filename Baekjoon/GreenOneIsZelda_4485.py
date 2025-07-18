import heapq

n = 0


def input_func():
    global n
    n = int(input())

    cave_map = []

    for _ in range(n):
        cave_map.append(list(map(int, input().split())))
    return cave_map


def dijkstra(cave_map):
    move_directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    cost_map = [[1e4 for _ in range(n)] for _ in range(n)]
    cost_map[0][0] = cave_map[0][0]

    queue = []
    heapq.heappush(queue, (cave_map[0][0], 0, 0))

    while queue:
        # 우선순위 큐를 활용하여 cost가 가장 낮은 경로를 추출
        cur_cost, x, y = heapq.heappop(queue)

        # 우선순위 큐를 활용하였기 때문에 최소값이 보장, 즉 가장 처음 도착했을때가 도착지점 cost의 최소값
        if x == n - 1 and y == n - 1:
            return cur_cost

        for mx, my in move_directions:
            nx, ny = x + mx, y + my
            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cur_cost + cave_map[nx][ny]
                # 새로운 cost가 현재 cost_map보다 작지 않은 경우 탐색 X
                if new_cost < cost_map[nx][ny]:
                    cost_map[nx][ny] = new_cost
                    heapq.heappush(queue, (new_cost, nx, ny))
    return None


def main():
    problem_times = 1
    while True:
        cave_map = input_func()
        if n == 0:
            return
        visited = [[False for _ in range(n)] for _ in range(n)]
        visited[0][0] = True
        answer = dijkstra(cave_map)
        print(f"Problem {problem_times}: {answer}")
        problem_times += 1


if __name__ == "__main__":
    main()
