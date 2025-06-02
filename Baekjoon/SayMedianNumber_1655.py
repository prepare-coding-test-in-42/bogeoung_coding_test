import sys
from heapq import *

input = sys.stdin.readline

def main():
    n = int(input())

    min_heap = []
    max_heap = []
    for _ in range(n):
        heappush(max_heap, -(int(input())))

        if min_heap and -max_heap[0] > min_heap[0]:
            to_min = heappop(max_heap)
            to_max = heappop(min_heap)

            heappush(min_heap, -to_min)
            heappush(max_heap, -to_max)

        if len(max_heap) - len(min_heap) >= 2:
            moving_values = heappop(max_heap)
            heappush(min_heap, -moving_values)
        elif len(min_heap) - len(max_heap) >= 2:
            moving_values = heappop(min_heap)
            heappush(max_heap, -moving_values)
        print(-max_heap[0])

        # print(f"min_heap : {min_heap}")
        # print(f"max_heap : {max_heap}")


if __name__ == "__main__":
    main()