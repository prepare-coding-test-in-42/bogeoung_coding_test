def input_func():
    n, l = map(int, input().split())

    road_map = [list(map(int, input().split())) for _ in range(n)]
    return n, l, road_map


def check_all_same_height(row):
    for i in range(len(row) - 1):
        if row[i] != row[i + 1]:
            return False
    return True


def check_able_to_ramp(row, n, l):
    used = [False] * n

    for i in range(n - 1):
        if row[i] == row[i + 1]:
            continue

        if row[i + 1] - row[i] == 1:
            if i - l + 1 < 0:  # 경사로를 놓을 공간이 없는 경우
                return False

            for j in range(i - l + 1, i + 1):
                if row[j] != row[i] or used[j]:  # 높이가 다르거나 이미 사용된 경우
                    return False
                used[j] = True

        elif row[i + 1] - row[i] == -1:
            if i + l >= n:
                return False

            for j in range(i + 1, i + l + 1):
                if row[j] != row[i + 1] or used[j]:
                    return False
                used[j] = True

        else:
            return False  # 높이 차이가 1 초과인 경우

    return True


def run(road_map, n, l):
    able_road_sum = 0
    for row in road_map:
        if check_all_same_height(row):
            able_road_sum += 1
        elif check_able_to_ramp(row, n, l):
            able_road_sum += 1

    return able_road_sum


def rotate_90(n, road_map):
    rotated_map = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated_map[j][n - i - 1] = road_map[i][j]
    return rotated_map


def main():
    n, l, road_map = input_func()
    answer = run(road_map, n, l)
    answer += run(rotate_90(n, road_map), n, l)
    print(answer)


if __name__ == "__main__":
    main()
