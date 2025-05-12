map_r, map_c = 0, 0

class Shark:
    def __init__(self, r,c,s,d,z):
        self.row = r
        self.col = c
        self.speed = s
        self.direction = d
        self.size = z

    def move(self):
        move_directions = [[0,0], [-1, 0], [1, 0], [0, 1], [0,-1]]

        exist_row, exist_col = self.row, self.col

        moving_count = self.speed
        while moving_count > 0:
            dr, dc = move_directions[self.direction]
            nr = self.row + dr
            nc = self.col + dc

            if nr < 0 or nr >= map_r or nc < 0 or nc >= map_c:
                self.turn_around()
                continue  # 이동하지 않고 다시 시도

            # 이동
            self.row, self.col = nr, nc
            moving_count -= 1
        
        return [[exist_row, exist_col], [self.row, self.col]]
    

    def turn_around(self):
        if self.direction == 1:
            self.direction = 2
        elif self.direction == 2:
            self.direction = 1
        elif self.direction ==3:
            self.direction = 4
        elif self.direction == 4:
            self.direction = 3
    
    

def input_func():
    global map_r, map_c
    map_r,map_c,m = map(int, input().split())

    sharkmap = [[[] for _ in range(map_c)] for _ in range(map_r)]
    sharks = []
    for _ in range(m):
        shark_r,shark_c,s,d,z = map(int, input().split())
        cur_shark = Shark(shark_r-1, shark_c-1, s,d,z)
        sharkmap[shark_r-1][shark_c-1].append(cur_shark)
        sharks.append(cur_shark)
    
    return sharkmap, sharks

def find_shark(shark_map, col):
    for i in range(len(shark_map)):
        if shark_map[i][col]:
            return shark_map[i][col].pop(0)
    return Shark(0,0,0,0,0)

def fight(sharks):
    sharks.sort(key = lambda shark : shark.size, reverse = True)
    return sharks[0]        

def shark_move(shark_map, sharks):
    global map_r, map_c
    next_map = [[[] for _ in range(map_c)] for _ in range(map_r)]

    for shark in sharks:
        _, [new_r, new_c] = shark.move()
        next_map[new_r][new_c].append(shark)

    # 겹치는 상어 정리
    new_sharks = []
    for i in range(map_r):
        for j in range(map_c):
            if next_map[i][j]:
                if len(next_map[i][j]) > 1:
                    next_map[i][j] = [fight(next_map[i][j])]
                new_sharks.append(next_map[i][j][0])

    # shark_map 덮어쓰기
    for i in range(map_r):
        for j in range(map_c):
            shark_map[i][j] = next_map[i][j]

    # sharks 리스트 갱신
    sharks.clear()
    sharks.extend(new_sharks)
    

def main():
    global map_c
    shark_map, sharks = input_func()
    king_row = 0
    answer = 0
    while king_row < map_c:
        catched_shark = find_shark(shark_map, king_row)
        if catched_shark.size > 0:
            for idx, shark in enumerate(sharks):
                if shark.size == catched_shark.size:
                    sharks.pop(idx)
                    break
        answer += catched_shark.size
        shark_move(shark_map, sharks)
        king_row += 1

    print(answer)




if __name__ == "__main__":
    main()
