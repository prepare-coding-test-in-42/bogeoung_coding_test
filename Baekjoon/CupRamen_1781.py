def input_func():
    n = int(input())

    ramens = []
    for _ in range(n):
        deadline, reward = map(int, input().split())
        ramens.append([deadline, reward])

    return ramens


def calc_max_ramen(ramens):
    ramens.sort(key=lambda x: [x[0], -x[1]])

    cur_time = 0
    ramen_index = 0
    earning_ramens = 0
    while cur_time <= ramens[-1][0]:
        if ramen_index >= len(ramens):
            return earning_ramens
        while cur_time >= ramens[ramen_index][0]:
            ramen_index += 1
            if ramen_index >= len(ramens):
                return earning_ramens
        print(f"earning {ramens[ramen_index][1]} ramens in {cur_time} and due is {ramens[ramen_index][0]}")
        earning_ramens += ramens[ramen_index][1]
        ramen_index += 1
        cur_time += 1

    return earning_ramens


def main():
    ramens = input_func()
    answer = calc_max_ramen(ramens)
    print(answer)


if __name__ == "__main__":
    main()
