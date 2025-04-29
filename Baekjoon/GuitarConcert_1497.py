from itertools import combinations

def input_func():
    n, m = map(int, input().split())

    guitar_infos = []
    for i in range(n):
        guitar_name, guitar_info = input().split()
        temp_infos = []
        for info in guitar_info:
            temp_infos.append(info)
        guitar_infos.append(temp_infos)
    return n, m, guitar_infos

def count_available_songs(m, guitars):
    total_songs = [False for _ in range(m)]
    for guitar in guitars:
        for idx, song in enumerate(guitar):
            if song == "Y":
                total_songs[idx] = True

    return total_songs.count(True)


def run(n, m, guitar_infos):
    max_comb_results_guitar_count = 0
    max_comb_results = 0
    for i in range(1, n+1):
        combs = combinations(guitar_infos, i)
        for comb in combs:
            available_songs = count_available_songs(m, comb)
            if available_songs == m:
                return i
            elif available_songs > max_comb_results:
                max_comb_results = available_songs
                max_comb_results_guitar_count = i


    if max_comb_results == 0:
        return -1
    else:
        return max_comb_results_guitar_count


def main():
    n, m, guitar_infos = input_func()
    answer = run(n, m, guitar_infos)
    print(answer)


if __name__ == "__main__":
    main()
