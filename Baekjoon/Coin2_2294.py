def input_func():
    n, k = map(int, input().split())

    coins = set()
    for _ in range(n):
        coins.add(int(input()))


    return k, sorted(list(coins), reverse= True)

def main():
    make_coin, coins = input_func()

    min_total_count = 100000

    while coins:
        remain_amount = make_coin
        coin_total_count = 0
        for coin in coins:
            cur_coin_count = remain_amount // coin
            coin_total_count += cur_coin_count
            remain_amount -= cur_coin_count * coin

            if remain_amount == 0:
                break

        if coin_total_count > 0:
            min_total_count = min(min_total_count, coin_total_count)
        coins.pop(0)
    if min_total_count == 10000:
        print("-1")
    else:
        print(min_total_count)

if __name__ == "__main__":
    main()