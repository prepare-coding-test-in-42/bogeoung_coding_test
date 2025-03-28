
def input_func():
    n, m = map(int, input().split())
    x, y, d = map(int, input().split())
    robot = Robot(x, y, d)
    room_map = [list(map(int, input().split())) for _ in range(n)]
    return n, m, robot, room_map


def run(n, m, robot, room_map):
    while True:
        if room_map[robot.x][robot.y] == 0:
            room_map[robot.x][robot.y] = -(robot.clean_count + 1)
            robot.clean_count += 1

        nearby_coordinates = robot.get_4direction_coordinate()  # 현재 좌표 기준 4방향의 좌표들
        is_cleaned_nearby_coordinates = [1, 1, 1, 1]
        for idx, coordinate in enumerate(nearby_coordinates):
            if 0 <= coordinate[0] < n and 0 <= coordinate[1] < m:
                if room_map[coordinate[0]][coordinate[1]] != 0:
                    is_cleaned_nearby_coordinates[idx] = 1
                else:
                    is_cleaned_nearby_coordinates[idx] = room_map[coordinate[0]][coordinate[1]]

        if sum(is_cleaned_nearby_coordinates) == 4:  # 청소되지 않은 빈 칸이 없는 경우
            move_x, move_y = nearby_coordinates[(robot.d + 2) % 4]
            if not (0 <= move_x < n and 0 <= move_y < m):
                return
            elif room_map[move_x][move_y] == 1:
                return
            else:
                robot.x, robot.y = move_x, move_y

        elif sum(is_cleaned_nearby_coordinates) != 4:  # 청소되지 않은 빈 칸이 있는 경우
            while True:
                robot.rotate_counter_clockwise_90()
                front_coordinate = nearby_coordinates[robot.d]
                if room_map[front_coordinate[0]][front_coordinate[1]] == 0:
                    robot.x, robot.y = front_coordinate[0], front_coordinate[1]
                    break


def main():
    n, m, robot, room_map = input_func()
    run(n, m, robot, room_map)
    print(robot.clean_count)


class Robot:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
        self.clean_count = 0

    def rotate_counter_clockwise_90(self):
        self.d = (self.d - 1) % 4

    def get_4direction_coordinate(self):
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 북, 동, 남, 서

        coordinates = []
        for direction in directions:
            coordinates.append([self.x + direction[0], self.y + direction[1]])
        return coordinates


if __name__ == "__main__":
    main()