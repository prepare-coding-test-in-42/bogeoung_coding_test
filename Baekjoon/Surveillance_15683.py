import copy
from itertools import product


class Camera:
    def __init__(self, i, j, type):
        self.x = i
        self.y = j
        self.direction = self.get_direction_by_type(type)
        self.rotate_times = 0

    def get_direction_by_type(self, type):  # 동, 남, 서, 북
        if type == 1:
            return [1, 0, 0, 0]
        elif type == 2:
            return [1, 0, 1, 0]
        elif type == 3:
            return [1, 0, 0, 1]
        elif type == 4:
            return [1, 0, 1, 1]
        elif type == 5:
            return [1, 1, 1, 1]

    def rotate_clockwise(self):
        temp_direction = copy.deepcopy(self.direction)
        temp_direction.insert(0, temp_direction.pop())
        self.direction = temp_direction

    def rotate_with_times(self, time):
        self.rotate_times = time
        for i in range(time):
            self.rotate_clockwise()

    def fill_map(self, map, direction_index, move_direction):
        x, y = self.x, self.y
        n, m = len(map), len(map[0])
        if self.direction[direction_index] == 1:
            while 0 <= x < n and 0 <= y < m and map[x][y] < 6:
                if map[x][y] == 0:
                    map[x][y] = -1
                x, y = x + move_direction[0], y + move_direction[1]

    def fill_map_4direction(self, map):
        move_directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for i in range(4):
            self.fill_map(map, i, move_directions[i])

        # print("inside_fill_map")
        # print_map( map)

    def revert_rotate(self):
        self.rotate_with_times(4 - self.rotate_times)


def print_map(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            print(f" {map[i][j]} ", end=" ")
        print()


def input_func():
    n, m = map(int, input().split())

    office_map = []
    for _ in range(n):
        office_map.append(list(map(int, input().split())))

    return n, m, office_map


def find_camera(n, m, map):
    cameras = []
    for i in range(n):
        for j in range(m):
            if 0 < map[i][j] < 6:
                cameras.append(Camera(i, j, map[i][j]))

    return cameras


def count_blind_space(cameras, office_map):
    temp_map = copy.deepcopy(office_map)
    for camera in cameras:
        camera.fill_map_4direction(temp_map)
        camera.revert_rotate()

    blind_space_count = 0
    for row in temp_map:
        blind_space_count += row.count(0)

    return blind_space_count


def run(n, m, office_map):
    answer = n * m + 1
    cameras = find_camera(n, m, office_map)
    combs = product('0123', repeat=len(cameras))

    for comb in combs:
        for rotate_times, camera in zip(list(comb), cameras):
            camera.rotate_with_times(int(rotate_times))
        answer = min(answer, count_blind_space(cameras, office_map))
        # print(f"answer is updated to {answer}, when {list(comb)}")
        if answer == 0:
            return answer
    return answer


def main():
    n, m, office_map = input_func()
    answer = run(n, m, office_map)
    print(answer)


if __name__ == "__main__":
    main()
