def input_func():
    n, m = map(int, input().split())

    ground_map = []
    for _ in range(n):
        ground_map.append(list(map(int, input().split())))

    move_methods = []
    for _ in range(m):
        move_methods.append(list(map(int, input().split())))

    return n, ground_map, move_methods


def update_location_with_bug(n, ground_map, x, y):
    move_directions = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
    update_count = 0
    for dx, dy in move_directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and ground_map[nx][ny] > 0:
            update_count += 1
    ground_map[x][y] += update_count


def make_new_clouds(ground_map, disappeared_locations):
    disappeared_set = set((x, y) for x, y in disappeared_locations)
    new_clouds_location = []
    for i in range(len(ground_map)):
        for j in range(len(ground_map[0])):
            if (i, j) not in disappeared_set and ground_map[i][j] >= 2:
                new_clouds_location.append([i, j])
                ground_map[i][j] -= 2
    return new_clouds_location


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


def main():
    n, ground_map, move_methods = input_func()
    answer = run(n, ground_map, move_methods)
    print(answer)


class Cloud:
    def __init__(self, n, location):
        self.n = n
        self.x = location[0]
        self.y = location[1]

    def move(self, dir_num, move_count):
        directions = [
            (0, -1), (-1, -1), (-1, 0), (-1, 1),
            (0, 1), (1, 1), (1, 0), (1, -1)
        ]

        dx, dy = directions[dir_num - 1]
        self.x = (self.x + dx * move_count) % self.n
        self.y = (self.y + dy * move_count) % self.n

    def rain(self, ground_map):
        ground_map[self.x][self.y] += 1


if __name__ == "__main__":
    main()
