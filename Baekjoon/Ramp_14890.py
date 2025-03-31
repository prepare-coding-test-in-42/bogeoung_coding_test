"""
1. 지도의 크기는 N * N
2. 길이란 한 행 또는 한 열 전부를 나타내며, 한쪽 끝에서 다른쪽 끝까지 가는 것이다.
3. 지나갈 수 있는 길의 개수를 구하려 한다.
4. 길을 지나갈 수 있으려면 모든 칸의 높이가 같아야 한다.
5. 지나갈 수 없는 길은 경사로를 놓아서 지나갈 수 있는 길을 만들 수 있다. 이 떄 경사로의 높이는 항상 1이며, 길이는 L이다.
6. 경사로는 낮은칸과 높은칸을 연결하며 아래 조건을 만족해야한다.
    6-1. 경사로는 낮은 칸에 놓이며, L개의 연속된 칸에 경사로의 바닥이 모두 접해야 한다.
    6-2. 낮은 칸과 높은 칸의 차이는 1이어야 한다.
    6-3. 경사로를 놓을 낮은 칸의 높이는 모두 같아야 한다.
7. 경사로를 놓을 수 없는 경우는 아래와 같다.
    7-1. 경사로를 놓은 곳에 또 놓을 경우
    7-2. 낮은 칸과 높은 칸의 차이가 1이 아닌 경우
    7-3. 낮은 칸의 높이가 모두 같지 않거나, L개가 연속되니 않은 경우
    7-4. 경사로를 놓다가 범위를 벗어나는 경우


TRY 1
- 모든 행, 모든 열에 대해서 아래 검사를 수행 -> rotate90함수 만들어서 수행?
    1. 모든 높이가 같은지
    2. 높이가 다른곳이 있다면 경사로를 놓을 수 있는지

"""


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
            if i - l + 1 < 0:
                return False

            for j in range(i - l + 1, i + 1):
                if row[j] != row[i] or used[j]:
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
            return False

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
