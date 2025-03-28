from collections import deque
import copy

EMPTY_SPACE_NUM = 0
WALL_NUM = 1
VIRUS_NUM = 2
answer = 0
def input_func():

    n, m = map(int, input().split())

    input_map = []
    for i in range(n):
        input_map.append(list(map(int, input().split())))

    return input_map, n, m

def run(lab, added_wall_count):
    global answer
    if added_wall_count == 3:
        lab.spread_virus()
        answer = max(answer, lab.count_safety_space())
        return

    for i in range(lab.n):
        for j in range(lab.m):
            if lab.map[i][j] == 0:
                lab.make_wall(i, j)
                run(lab, added_wall_count + 1)
                lab.break_wall(i, j)


def main():
    global answer
    input_map, n, m = input_func()
    lab = LAB(input_map, n, m)
    run(lab, 0)
    print(answer)
    return answer

class LAB:
    move_direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    def __init__(self, lab_map, n, m):
        self.map = lab_map
        self.n = n
        self.m = m
        self.spread_virus_map = []
        self.init_virus_queue = deque()

    def make_wall(self, i, j):
        self.map[i][j] = WALL_NUM

    def break_wall(self, i, j):
        self.map[i][j] = EMPTY_SPACE_NUM
    def spread_virus(self):
        self.spread_virus_map = copy.deepcopy(self.map)
        for i in range(self.n):
            for j in range(self.m):
                if self.spread_virus_map[i][j] == VIRUS_NUM:
                    self.init_virus_queue.append([i,j])

        while self.init_virus_queue:
            cur_x, cur_y = self.init_virus_queue.popleft()
            for direction in self.move_direction:
                new_x, new_y = cur_x + direction[0], cur_y + direction[1]
                if 0<= new_x <self.n and 0<= new_y < self.m:
                    if self.spread_virus_map[new_x][new_y] == EMPTY_SPACE_NUM :
                        self.spread_virus_map[new_x][new_y] = VIRUS_NUM
                        self.init_virus_queue.append([new_x, new_y])

    def count_safety_space(self):
        safety_space_count = 0
        for i in range(self.n):
            safety_space_count += self.spread_virus_map[i].count(EMPTY_SPACE_NUM)
        return safety_space_count


if __name__ == "__main__":
    main()