def main():
    n = int(input())
    stairs = list(map(int, input().split()))

    max_dp = stairs[:]
    min_dp = stairs[:]

    for i in range(1, n):
        a, b, c = map(int, input().split())

        prev_max = max_dp[:]
        max_dp[0] = max(prev_max[0], prev_max[1]) + a
        max_dp[1] = max(prev_max) + b
        max_dp[2] = max(prev_max[1], prev_max[2]) + c

        prev_min = min_dp[:]
        min_dp[0] = min(prev_min[0], prev_min[1]) + a
        min_dp[1] = min(prev_min) + b
        min_dp[2] = min(prev_min[1], prev_min[2]) + c

    print(max(max_dp), min(min_dp))


if __name__ == "__main__":
    main()
