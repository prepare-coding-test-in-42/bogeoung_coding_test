def bfs(maps):
    move_direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    queue = [[0, 0, 1]]

    while queue:
        curx, cury, count = queue.pop(0)
        if curx == len(maps) - 1 and cury == len(maps[0]) - 1:
            return count

        for move in move_direction:
            newx, newy = curx + move[0], cury + move[1]
            if newx < 0 or newx >= len(maps) or newy < 0 or newy >= len(maps[0]):
                continue
            if maps[newx][newy] == 1:
                queue.append([newx, newy, count + 1])
                maps[newx][newy] = 2
    return -1


def solution(maps):
    return bfs(maps)