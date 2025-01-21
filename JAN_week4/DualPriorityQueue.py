import heapq
def solution(operations):
    answer = [0, 0]
    heap, maxHeap = [], []
    heapq.heapify(heap)
    heapq.heapify(maxHeap)

    for operation in operations:
        sign, number = operation.split()
        if sign == "I":
            heapq.heappush(heap, int(number))
            heapq.heappush(maxHeap, -(int(number)))
        elif sign == "D" and len(heap) > 0 and len(maxHeap) > 0:
            if "-" in number:
                pop_num = heapq.heappop(heap)
                maxHeap.remove(-pop_num)
                heapq.heapify(maxHeap)
            else:
                pop_num = heapq.heappop(maxHeap)
                heap.remove(-pop_num)
                heapq.heapify(heap)

    if len(heap) > 0:
        answer = [-heapq.heappop(maxHeap), heapq.heappop(heap)]

    return answer