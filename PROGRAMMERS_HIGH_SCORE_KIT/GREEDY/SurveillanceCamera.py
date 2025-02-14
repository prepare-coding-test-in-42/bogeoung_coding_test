def solution(routes):
    routes.sort(key=lambda x: x[1])

    answer = 1
    cur_camera = routes[0][1]
    for i in range(1, len(routes)):
        if cur_camera >= routes[i][0] and cur_camera <= routes[i][1]:
            continue
        else:
            answer += 1
            cur_camera = routes[i][1]

    return answer