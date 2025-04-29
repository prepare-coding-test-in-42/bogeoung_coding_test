def input_func():
    n, l, r = map(int, input().split())

    population_map = []
    for i in range(n):
        population_map.append(list(map(int, input().split())))

    return n, l, r, population_map


def make_union(i, j, n, l, r, visited, population_map):
    move_directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    queue = [[i, j]]
    unions = [[i, j]]
    while queue:
        x, y = queue.pop(0)
        for move_x, move_y in move_directions:
            new_x = x + move_x
            new_y = y + move_y
            if 0 <= new_x < n and 0 <= new_y < n and not visited[new_x][new_y]:
                if l <= abs(population_map[x][y] - population_map[new_x][new_y]) <= r:
                    visited[x + move_x][y + move_y] = True
                    queue.append([x + move_x, y + move_y])
                    unions.append([x + move_x, y + move_y])
    return unions


def update_unions(unions, population_map):
    union_population = sum(population_map[x][y] for x, y in unions) // len(unions)
    for x, y in unions:
        population_map[x][y] = union_population


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


def main():
    n, l, r, population_map = input_func()
    answer = run(n, l, r, population_map)
    print(answer)


if __name__ == "__main__":
    main()
