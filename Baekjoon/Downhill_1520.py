import sys
sys.setrecursionlimit(10**9)

maps = []
answer = 0
move_directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def input_func():
    global m, n, maps
    m, n = map(int, input().split())

    maps = []
    for _ in range(m):
        maps.append(list(map(int, input().split())))


def dfs(cur_x, cur_y, dp):
    if cur_x == m-1 and cur_y == n-1:
        return 1

    if dp[cur_x][cur_y] != -1:
        return dp[cur_x][cur_y]

    dp[cur_x][cur_y] = 0
    for direction in move_directions:
        new_x, new_y = cur_x + direction[0], cur_y + direction[1]
        if 0 <= new_x < m and 0 <= new_y < n and maps[new_x][new_y] < maps[cur_x][cur_y]:
            dp[cur_x][cur_y] += dfs(new_x, new_y, dp)

    return dp[cur_x][cur_y]



def main():
    input_func()
    dp = [[-1 for _ in range(n)] for _ in range(m)]
    dfs(0, 0, dp)
    print(dp[0][0])


if __name__ == "__main__":
    main()
