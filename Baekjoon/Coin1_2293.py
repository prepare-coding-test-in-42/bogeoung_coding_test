
def input_func():
    n, k = map(int, input().split())

    coins = []
    for _ in range(n):
        coins.append(int(input()))
    coins.sort()
    return k, coins


def dp(make_num, coins):
    dp_list = [0 for _ in range(make_num + 1)]
    dp_list[0] = 1

    for coin in coins:
        for i in range(coin, make_num + 1):
            dp_list[i] += dp_list[i-coin]
    return dp_list[make_num]


def main():
    make_num, coins = input_func()
    print(dp(make_num, coins))

if __name__ == "__main__":
    main()