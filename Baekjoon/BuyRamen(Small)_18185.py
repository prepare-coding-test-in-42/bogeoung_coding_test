def greedy(n, ramen_cnt_to_buy):
    cost = 0
    for i in range(n):
        if ramen_cnt_to_buy[i] == 0:
            continue
        if i + 2 < n:
            # i+1 공장 라면이 i+2 공장보다 많으면,
            # 3개 묶음 구매를 위해 차이만큼 2개 묶음 먼저 구매
            if ramen_cnt_to_buy[i + 1] > ramen_cnt_to_buy[i + 2]:
                cnt = min(ramen_cnt_to_buy[i], ramen_cnt_to_buy[i + 1] - ramen_cnt_to_buy[i + 2])
                ramen_cnt_to_buy[i] -= cnt
                ramen_cnt_to_buy[i + 1] -= cnt
                cost += cnt * 5

            # 3개 묶음 구매
            cnt = min(ramen_cnt_to_buy[i], ramen_cnt_to_buy[i + 1], ramen_cnt_to_buy[i + 2])
            ramen_cnt_to_buy[i] -= cnt
            ramen_cnt_to_buy[i + 1] -= cnt
            ramen_cnt_to_buy[i + 2] -= cnt
            cost += cnt * 7

        # 2개 묶음 구매
        if i + 1 < n:
            cnt = min(ramen_cnt_to_buy[i], ramen_cnt_to_buy[i + 1])
            ramen_cnt_to_buy[i] -= cnt
            ramen_cnt_to_buy[i + 1] -= cnt
            cost += cnt * 5

        # 마지막으로 남은 것만 단일 처리
        if ramen_cnt_to_buy[i] > 0:
            cost += ramen_cnt_to_buy[i] * 3
            ramen_cnt_to_buy[i] = 0
    return cost


def main():
    n = int(input())
    ramen_cnt_to_buy = list(map(int, input().split()))
    answer = greedy(n, ramen_cnt_to_buy)
    print(answer)


if __name__ == "__main__":
    main()
