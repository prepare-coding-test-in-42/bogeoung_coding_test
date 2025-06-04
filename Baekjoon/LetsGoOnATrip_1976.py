import copy

n, m = 0, 0
goal = []
answer = ""


def input_func():
    global n, m, goal
    n = int(input())
    m = int(input())

    roads = []

    for _ in range(n):
        roads.append(list(map(int, input().split())))

    goal = list(map(int, input().split()))

    for idx, nation_num in enumerate(goal):
        goal[idx] = nation_num - 1

    return roads


def map_update(roads):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if roads[i][k] and roads[k][j]:
                    roads[i][j] = 1


def run(roads):
    global goal
    is_possible = True

    map_update(roads)

    for i in range(len(goal) - 1):
        first_goal = goal[i]
        next_goal = goal[i - 1]
        if first_goal == next_goal:
            continue
        if roads[first_goal][next_goal]:
            continue
        else:
            is_possible = False
    if is_possible:
        return "YES"
    return "NO"


def main():
    roads = input_func()
    answer = run(roads)
    print(answer)


if __name__ == "__main__":
    main()
