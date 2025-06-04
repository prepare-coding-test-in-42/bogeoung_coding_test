def input_func():
    n, k = map(int, input().split())

    durability = list(map(int, input().split()))

    return n, k, durability

def rotate(list):
    rotated_list = list[:]
    rotated_list.insert(0, rotated_list.pop())
    return rotated_list


def move_robot(n, convey_belt, durability):
    for idx in range(len(convey_belt)-1, -1, -1):
        if convey_belt[n-1] >= 1:
            convey_belt[n-1] -= 1
        if convey_belt[idx] == 0:
            continue
        if idx == len(convey_belt) -1:
            if convey_belt[0] == 0 and durability[0] >= 1:
                convey_belt[idx] -= 1
                convey_belt[0] += 1
                durability[0] -=1
            else:
                continue
        elif convey_belt[idx] >= 1:
            if convey_belt[idx+1] == 0 and durability[idx+1] >= 1:
                convey_belt[idx+1] += 1
                convey_belt[idx] -= 1
                durability[idx+1] -= 1
            else:
                continue
        else:
            return False, convey_belt, durability
    return True, convey_belt, durability



def run(n, k, durability):
    answer = 1
    convey_belt = [0 for _ in range(2 * n)]
    while True:
        durability = rotate(durability)
        convey_belt = rotate(convey_belt)
        flag, convey_belt, durability = move_robot(n,convey_belt, durability)
        if not flag:
            return answer

        if convey_belt[n -1] == 1:
            convey_belt[n-1] = 0
        if convey_belt[0] == 0 and durability[0] >= 1:
            convey_belt[0] += 1
            durability[0] -= 1

        if durability.count(0) >= k:
            return answer
        answer += 1



def main():
    n, k, durability = input_func()
    answer = run(n,k,durability)
    print(answer)

if __name__== "__main__":
    main()
