answer = 0
visited = []


def bfs(start_idx, computers):
    global answer
    global visited
    if start_idx in visited:
        return

    queue = [start_idx]
    while (queue):
        cur_com = queue.pop(0)
        visited.append(cur_com)
        connect_infos = computers[cur_com]
        for idx, connect_info in enumerate(connect_infos):
            if connect_info == 1 and idx not in visited:
                queue.append(connect_info)
    answer += 1


def solution(n, computers):
    for i in range(n):
        bfs(i, computers)
    return answer

solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])