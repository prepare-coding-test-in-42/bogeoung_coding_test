from collections import deque


class BlockGroup:
    def __init__(self):
        self.blocks = []
        self.standard_block = [-1, -1]

    def add_block(self, block_x, block_y, is_rainbow=False):
        self.blocks.append([block_x, block_y, is_rainbow])

    def set_standard_block(self):
        only_color_blocks = [block for block in self.blocks if block[2] == False]
        only_color_blocks.sort(key=lambda x: [x[0], x[1]])
        self.standard_block = only_color_blocks[0]

    def get_group_size(self):
        return len(self.blocks)

    def get_rainbow_count(self):
        rainbow_blocks = [block for block in self.blocks if block[2] == True]
        return len(rainbow_blocks)


n = 0


def input_func():
    global n
    n, m = map(int, input().split())

    block_map = []
    for _ in range(n):
        block_map.append(list(map(int, input().split())))

    return block_map


def make_group(block_map, i, j, color_index, visited):
    move_directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    queue = deque()
    queue.append([i, j])

    block_group = BlockGroup()
    while queue:
        cur_x, cur_y = queue.popleft()
        block_group.add_block(cur_x, cur_y, block_map[cur_x][cur_y] == 0)
        visited[cur_x][cur_y] = True
        for direction in move_directions:
            new_x, new_y = cur_x + direction[0], cur_y + direction[1]
            if 0 <= new_x < n and 0 <= new_y < n and visited[new_x][new_y] == False:
                if block_map[new_x][new_y] in [color_index, 0]:
                    visited[new_x][new_y] = True
                    queue.append([new_x, new_y])
    block_group.set_standard_block()
    return block_group


def find_groups(block_map):
    groups = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False and block_map[i][j] not in [-1, 0, 9]:
                cur_group = make_group(block_map, i, j, block_map[i][j], visited)
                # 무지개 블럭에 대한 방문 처리 취소
                for block in cur_group.blocks:
                    if block_map[block[0]][block[1]] == 0:
                        visited[block[0]][block[1]] = False
                groups.append(cur_group)
    groups.sort(key=lambda group: [-group.get_group_size(), -group.get_rainbow_count(), -group.standard_block[0],
                                   -group.standard_block[1]])
    return groups


def get_nearest_block(block_map, start_row, col_index):
    for row_index in range(start_row, -1, -1):
        row = block_map[row_index]
        if row[col_index] == -1:
            return [row_index, 9]
        elif row[col_index] == 9:
            continue
        return [row_index, row[col_index]]
    return [9, 9]


def apply_gravity(block_map):
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if block_map[i][j] == 9:
                row_index, numbers = get_nearest_block(block_map, i, j)
                if numbers == 9:
                    continue
                block_map[i][j] = numbers
                block_map[row_index][j] = 9


def rotate_counter_clockwise(block_map):
    counter_clockwise_map = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            counter_clockwise_map[n - j - 1][i] = block_map[i][j]
    return counter_clockwise_map


def run(block_map):
    answer = 0
    while True:
        # 그룹을 찾음
        groups = find_groups(block_map)
        # 그룹이 존재하지 않은 경우 break
        if len(groups) <= 0:
            return answer
        # 크기가 가장 큰 그룹을 선정
        selected_group = groups.pop(0)
        if len(selected_group.blocks) < 2:
            return answer
        # 그룹의 크기 ^ 2만큼 점수 획득 & 방문 처리
        answer += selected_group.get_group_size() ** 2
        for block in selected_group.blocks:
            block_map[block[0]][block[1]] = 9

        # 격자에 중력 작용
        apply_gravity(block_map)

        # 격자를 반시계 방향으로 회전
        block_map = rotate_counter_clockwise(block_map)
        # 격자에 중력 작용
        apply_gravity(block_map)


def main():
    block_map = input_func()
    answer = run(block_map)
    print(answer)


if __name__ == "__main__":
    main()
