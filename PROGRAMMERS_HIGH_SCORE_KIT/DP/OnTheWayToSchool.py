def solution(m, n, puddles):
    map = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n): # 행
        for j in range(m): # 열
            if i == 0 and j == 0:
                map[i][j] = 1
            elif [j+1, i+1] in puddles:
                continue
            elif j == 0:
                map[i][j] = map[i-1][j]
            elif i == 0:
                map[i][j] = map[i][j-1]
            else:
                map[i][j] = map[i-1][j] +  map[i][j-1]
    
    return map[i][j] % 1000000007
    