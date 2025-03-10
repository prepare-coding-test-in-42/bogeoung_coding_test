def solution(n, results):
    answer = 0
    map = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for winner, loser in results:
        map[winner][loser] = 1
        map[loser][winner] = -1

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    continue
                if map[i][k] == map[k][j] == 1:
                    map[i][j] = 1
                    map[j][i] = map[j][k] = map[k][i] = -1
    for row in map:
        if row.count(0) == 2:
            answer += 1

    return answer