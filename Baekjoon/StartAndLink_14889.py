from itertools import combinations
answer = 100*21

def input_func():
    n = int(input())
    synergy_map = [list(map(int, input().split())) for _ in range(n)]

    return n, synergy_map

def make_other_team(selected_numbers, total_numbers):
    start_team = list(selected_numbers)
    link_team = []

    for num in total_numbers:
        if num not in start_team:
            link_team.append(num)

    return link_team

def sum_synergy(selected_numbers, synergy_map):
    synergy_comb = combinations(selected_numbers, 2)
    synergy_sum = 0
    for comb in synergy_comb:
        synergy_sum += synergy_map[comb[0]][comb[1]]
        synergy_sum += synergy_map[comb[1]][comb[0]]
    return synergy_sum

def run(n, synergy_map):
    global answer

    total_numbers = [i for i in range(n)]
    combs = combinations(total_numbers, int(n/2))
    for start_team in combs:
        link_team = make_other_team(start_team, total_numbers)
        synergy_sum_diff = abs(sum_synergy(start_team, synergy_map) - sum_synergy(link_team, synergy_map))
        answer = min(answer, synergy_sum_diff)

    print(answer)

def main():
    global answer
    n, synergy_map = input_func()
    run(n, synergy_map)


if __name__ == "__main__":
    main()