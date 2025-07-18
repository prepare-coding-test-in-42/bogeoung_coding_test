def input_func():
    n, k = map(int, input().split())

    coins = set()
    for _ in range(n):
        coins.add(int(input()))


    return k, sorted(list(coins), reverse= True)


def dp(make_coin, coins):
    dp_list = [[] for _ in range(make_coin + 1)]
    dp_list[0] = [[0]]

    for coin in coins:
        for i in range(coin, make_coin + 1):
            for before_list in dp_list[i-coin]:
                candidate_list = before_list[:]
                candidate_list.append(coin)
                dp_list[i].append(candidate_list)

    min_length = len(dp_list[make_coin][0])

    for candidate_list in dp_list[make_coin]:
        if len(candidate_list) < min_length:
            min_length = len(candidate_list)
    return min_length - 1

def main():
    make_coin, coins = input_func()
    print(dp(make_coin, coins))

if __name__ == "__main__":
    main()