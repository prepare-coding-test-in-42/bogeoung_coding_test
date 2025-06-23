def input_func():
    n = int(input())

    coins = dict()
    for _ in range(n):
        amount, count = map(int, input().split())
        coins[amount] = count
    return dict(sorted(coins.items(), key=lambda x: -x[0]))


def calc_total_sum(coins):
    total_sum = 0
    for coin, count in coins.items():
        total_sum += coin * count

    return total_sum


def run(coins):
    total_sum = calc_total_sum(coins)
    if total_sum % 2 != 0:
        return 0

    can_make_values_dp = [-1 for _ in range(total_sum + 1)]
    can_make_values_dp[0] = 0

    for coin, count in coins.items():
        for i in range(total_sum + 1):
            if can_make_values_dp[i] >= 0:
                can_make_values_dp[i] = count
            elif i >= coin and can_make_values_dp[i - coin] > 0:
                can_make_values_dp[i] = can_make_values_dp[i - coin] - 1

    if can_make_values_dp[total_sum // 2] >= 0:
        return 1
    else:
        return 0


def main():
    for _ in range(3):
        coins = input_func()
        print(run(coins))


if __name__ == "__main__":
    main()
