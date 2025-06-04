class Blocks:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.map = [[0 for _ in range(self.col)] for _ in range(self.row)]

    def count_filled_block(self):
        return sum(row.count(1) for row in self.map)

    def add_block(self, blocks):
        pass

    def count_filled_block(self):
        block_count = 0
        for row in self.map:
            block_count += row.count(1)
        return block_count


class Green(Blocks):
    def __init__(self):
        super().__init__(6, 4)

    def add_block(self, blocks):
        move_x = -1
        while True:
            moved = [[r + move_x + 1, c] for r, c in blocks]
            if any(r >= self.row or self.map[r][c] != 0 for r, c in moved):
                break
            move_x += 1

        for r, c in blocks:
            self.map[r + move_x][c] = 1

    def check_rows(self):
        full_filled_rows = []
        for row_index in range(self.row):
            if sum(self.map[row_index]) == self.col:
                full_filled_rows.append(row_index)

        for index in sorted(full_filled_rows):
            self.map.pop(index)
            self.map.insert(0, [0 for _ in range(self.col)])
        return len(full_filled_rows)

    def check_light_row(self):
        remove_count = 0
        for row_index in range(1, -1, -1):
            if 1 in self.map[row_index]:
                remove_count += 1

        while remove_count > 0:
            self.map.pop()  # 마지막 행 제거
            self.map.insert(0, [0 for _ in range(self.col)])  # 새로운 행 추가
            remove_count -= 1


class Blue(Blocks):
    def __init__(self):
        super().__init__(4, 6)

    def rotate_clockwise(self):
        self.map = [list(reversed(col)) for col in zip(*self.map)]

    def rotate_counter_clockwise(self):
        self.map = [list(row) for row in zip(*self.map)][::-1]

    def add_block(self, blocks):
        move_y = -1
        while True:
            moved = [[r, c + move_y + 1] for r, c in blocks]
            if any(c >= self.col or self.map[r][c] != 0 for r, c in moved):
                break
            move_y += 1

        for r, c in blocks:
            self.map[r][c + move_y] = 1

    def check_cols(self):
        full_filled_cols = []
        for col_index in range(self.col):
            if all(self.map[row_index][col_index] == 1 for row_index in range(self.row)):
                full_filled_cols.append(col_index)

        for index in sorted(full_filled_cols):
            for row_index in range(self.row):
                self.map[row_index].pop(index)
                self.map[row_index].insert(0, 0)
        return len(full_filled_cols)

    def check_light_col(self):
        remove_count = 0
        for col_index in range(1, -1, -1):
            for row_index in range(self.row):
                if self.map[row_index][col_index] == 1:
                    remove_count += 1
                    break

        while remove_count > 0:
            for row_index in range(self.row):
                self.map[row_index].pop()  # 마지막 행 제거
                self.map[row_index].insert(0, 0)  # 새로운 행 추가
            remove_count -= 1

    def count_filled_block(self):
        self.rotate_clockwise()
        return super().count_filled_block()


def input_func():
    n = int(input())

    orders = []
    for _ in range(n):
        orders.append(list(map(int, input().split())))

    return orders


def run(orders):
    block_types = [[[0, 0]], [[0, 0]], [[0, 0], [0, 1]], [[0, 0], [1, 0]]]
    blue_blocks = Blue()
    green_blocks = Green()
    score = 0
    for t, x, y in orders:
        green_added_blocks = []
        blue_added_blocks = []
        for direction in block_types[t]:
            green_added_blocks.append([direction[0], y + direction[1]])
            blue_added_blocks.append([x + direction[0], direction[1]])

        green_blocks.add_block(green_added_blocks)
        blue_blocks.add_block(blue_added_blocks)

        score += green_blocks.check_rows()
        score += blue_blocks.check_cols()

        green_blocks.check_light_row()
        blue_blocks.check_light_col()

    return [score, blue_blocks.count_filled_block() + green_blocks.count_filled_block()]


def main():
    orders = input_func()
    score, filled_block_count = run(orders)
    print(score)
    print(filled_block_count)


if __name__ == "__main__":
    main()
