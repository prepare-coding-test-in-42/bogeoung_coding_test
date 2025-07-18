n, m = 0, 0
max_value = 0


def input_func():
    global n, m
    n, m = map(int, input().split())

    mars_map = []
    for _ in range(n):
        mars_map.append(list(map(int, input().split())))

    return mars_map


def calc_cost(mars_map, costs):
    # 첫번째 행은 오른쪽으로만 이동 가능하기 때문에 누적합으로 초기화
    costs[0][0] = mars_map[0][0]
    for j in range(1, m):
        costs[0][j] = costs[0][j - 1] + mars_map[0][j]

    for i in range(1, n):
        left_dp = [0 for _ in range(m)]
        right_dp = [0 for _ in range(m)]

        # 현재 행의 각 칸으로 오기 위한 두가지 방향을 고려 (왼->오 / 오->왼)
        # 왼쪽으로 이동하는 경우의 첫열, 오른쪽으로 이동하는 경우의 마지막열을 초기화
        left_dp[0] = costs[i - 1][0] + mars_map[i][0]
        right_dp[-1] = costs[i - 1][-1] + mars_map[i][-1]

        # 왼쪽으로만 이동하는 경우
        for j in range(1, m):
            left_dp[j] = max(costs[i - 1][j], left_dp[j - 1]) + mars_map[i][j]

        # 오른쪽으로만 이동하는 경우
        for j in range(m - 2, -1, -1):
            right_dp[j] = max(costs[i - 1][j], right_dp[j + 1]) + mars_map[i][j]

        # 두 방향 중 더 큰값으로 갱신
        for j in range(m):
            costs[i][j] = max(right_dp[j], left_dp[j])

    return costs[-1][-1]


def main():
    mars_map = input_func()
    costs = [[0 for _ in range(m)] for _ in range(n)]
    costs[0][0] = mars_map[0][0]
    answer = calc_cost(mars_map, costs)
    print(answer)


if __name__ == "__main__":
    main()
