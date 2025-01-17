import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        if scoville[0] >= K:
            break
        if(len(scoville) <= 1):
            return -1
        newFood = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, newFood)
        answer += 1
    return answer