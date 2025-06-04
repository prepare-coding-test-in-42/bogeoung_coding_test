n = 0
max_cracked_num = 0

INDEX_NUM = 0
DURABILITY_NUM = 1
WEIGHT_NUM = 2


def input_func():
    global n
    n = int(input())

    eggs = []
    for i in range(n):
        d, w = map(int, input().split())
        eggs.append([i, d, w])
    return eggs


def dfs(eggs, cur_egg_index, cracked_count):
    global max_cracked_num

    if cur_egg_index == n:
        max_cracked_num = max(max_cracked_num, cracked_count)
        return

    cur_egg = eggs[cur_egg_index]
    if cur_egg[DURABILITY_NUM] <= 0:
        dfs(eggs, cur_egg_index + 1, cracked_count)
        return

    is_fight = False
    for i in range(n):
        if i == cur_egg_index or eggs[i][DURABILITY_NUM] <= 0:
            continue
        is_fight = True
        cur_egg[DURABILITY_NUM] -= eggs[i][WEIGHT_NUM]
        eggs[i][DURABILITY_NUM] -= cur_egg[WEIGHT_NUM]

        new_cracked = 0
        if cur_egg[DURABILITY_NUM] <= 0:
            new_cracked += 1
        if eggs[i][DURABILITY_NUM] <= 0:
            new_cracked += 1
        dfs(eggs, cur_egg_index + 1, cracked_count + new_cracked)
        cur_egg[DURABILITY_NUM] += eggs[i][WEIGHT_NUM]
        eggs[i][DURABILITY_NUM] += cur_egg[WEIGHT_NUM]

    if not is_fight:
        dfs(eggs, cur_egg_index + 1, cracked_count)


def main():
    global max_cracked_num
    eggs = input_func()
    dfs(eggs, 0, 0)
    print(max_cracked_num)


if __name__ == "__main__":
    main()
