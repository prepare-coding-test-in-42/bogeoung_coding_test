def input_func():
    n, k = map(int, input().split())

    coins = set()
    for _ in range(n):
        coins.add(int(input()))


    return k, sorted(list(coins), reverse= True)


def dp(make_coin, coins):
    dp_list = [1000000 for _ in range(make_coin + 1)]
    dp_list[0] = 0

    for coin in coins:
        for i in range(coin, make_coin + 1):
            dp_list[i] = min(dp_list[i], dp_list[i-coin] + 1)


    if dp_list[make_coin] == 1000000:
        return -1
    return dp_list[make_coin]

def main():
    make_coin, coins = input_func()
    print(dp(make_coin, coins))

if __name__ == "__main__":
    main()