from collections import deque


class Taxi:
    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.remain_fuel = n

    def move(self, dest_x, dest_y, distance):
        self.x = dest_x
        self.y = dest_y
        self.remain_fuel -= distance

    def fill_fuel(self, distance):
        self.remain_fuel += distance * 2

class Customer:
    def __init__(self, x, y, dest_x, dest_y):
        self.x = x
        self.y = y
        self.dest_x = dest_x
        self.dest_y = dest_y


n = 0
def input_func():
    global n
    n, m, init_fuel = map(int, input().split())
    road_map = []

    for _ in range(n):
        road_map.append(list(map(int, input().split())))

    taxi_start_x, taxi_start_y = map(int, input().split())
    taxi = Taxi(taxi_start_x - 1, taxi_start_y - 1, init_fuel)

    customers = []
    for _ in range(m):
        start_x, start_y, dest_x, dest_y = map(int, input().split())
        customers.append(Customer(start_x - 1, start_y - 1, dest_x - 1, dest_y - 1))
    customers.sort(key = lambda customer : [customer.x, customer.y])
    return road_map, taxi, customers

def calc_distance(road_map, cur_x, cur_y):
    queue = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]
    move_directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    dist_map = [[0 for _ in range(n)] for _ in range(n)]
    queue.append([cur_x, cur_y, 0])
    while queue:
        cur_x, cur_y,cur_move_count = queue.popleft()
        visited[cur_x][cur_y] = True
        dist_map[cur_x][cur_y] = cur_move_count
        for direction in move_directions:
            new_x, new_y = cur_x + direction[0], cur_y + direction[1]
            if 0 <= new_x < n and 0 <= new_y < n and road_map[new_x][new_y] == 0 and visited[new_x][new_y] == False:
                visited[new_x][new_y] = True
                queue.append([new_x, new_y, cur_move_count + 1])
    return dist_map

def pick_customer(road_map,taxi_x, taxi_y, customers):
    distances = []
    dist_map = calc_distance(road_map, taxi_x, taxi_y)
    for idx, customer in enumerate(customers):
        if customer.x == taxi_x and customer.y == taxi_y:
            distances.append(0)
        elif dist_map[customer.x][customer.y] == 0:
            distances.append(n*n*2)
        else:
            distances.append(dist_map[customer.x][customer.y])

    min_distance = min(distances)
    if min_distance != n*n*2:
        for idx, distance in enumerate(distances):
            if distance == min_distance:
                return [customers.pop(idx), distance]
    return [0, 0]


def run(road_map, taxi, customers):
    while True:
        if taxi.remain_fuel <= 0 and len(customers) > 0:
            return -1
        elif len(customers) <= 0:
            return taxi.remain_fuel

        # 가장 가까이 있는 손님을 찾음
        picked_customer, move_distance = pick_customer(road_map, taxi.x, taxi.y, customers)
        if picked_customer == 0:
            return -1
        # print(f"picked_customer : {picked_customer}, move_distance : {move_distance}")

        # 손님을 픽업
        taxi.move(picked_customer.x, picked_customer.y, move_distance)
        # print(f"after move taxi's location : [{taxi.x},{taxi.y}]")
        if taxi.remain_fuel <= 0:
            return -1

        # 손님을 목적지까지 이동
        cur_customer_dist_map = calc_distance(road_map,taxi.x, taxi.y)

        to_destination_distance = cur_customer_dist_map[picked_customer.dest_x][picked_customer.dest_y]
        if taxi.x != picked_customer.dest_x and taxi.y != picked_customer.dest_y and to_destination_distance == 0:
            return -1
        taxi.move(picked_customer.dest_x, picked_customer.dest_y, to_destination_distance)
        if taxi.remain_fuel < 0:
            return -1

        # 연료 충전
        taxi.fill_fuel(to_destination_distance)


def main():
    road_map, taxi, customers = input_func()
    answer = run(road_map, taxi, customers)
    print(answer)

if __name__== "__main__":
    main()

