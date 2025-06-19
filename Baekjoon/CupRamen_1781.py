import heapq

def input_func():
    global n
    n = int(input())

    ramens = []
    for _ in range(n):
        deadline, reward = map(int, input().split())
        ramens.append([deadline, reward])

    return ramens

def calc_max_ramen(ramens):
    heap = []

    for deadline, reward in ramens:
        heapq.heappush(heap, reward)
        if len(heap) > deadline:
            heapq.heappop(heap)

    return sum(heap)


def main():
    ramens = input_func()
    answer = calc_max_ramen(ramens)
    print(answer)


if __name__ == "__main__":
    main()
