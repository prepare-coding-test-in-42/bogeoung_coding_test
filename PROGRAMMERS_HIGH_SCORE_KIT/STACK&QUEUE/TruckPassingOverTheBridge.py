
def updateBridge(BridgeLength, num):
    '''
    :param BridgeLength: 남은 이동거리 값을 업데이트 시킬 다리
    :param num: 이동거리 값을 얼만큼 감소시킬지 나타내는 값
    :return: 값을 감소시킨 Bridge 리스트
    '''
    for i in range(len(BridgeLength)):
        BridgeLength[i] -= num
    return BridgeLength


def solution(bridge_length, weight, truck_weights):
    answer = 1
    curBridgeWeight = []  # 현재 다리 위에 있는 트럭의 무게
    curBridgeLength = []  # 현대 다리 위에 있는 트럭들의 남은 움직일 길이

    for truck in truck_weights:
        # 다리에 트럭이 추가가 불가능한 경우
        if sum(curBridgeWeight) + truck > weight:
            while (sum(curBridgeWeight) > weight - truck):
                # 가장 먼저 들어간 트럭부터 모두 지나도록 계산
                frontOfBridgeLength = curBridgeLength.pop(0)
                answer += frontOfBridgeLength
                curBridgeWeight.pop(0)
                curBridgeLength = updateBridge(curBridgeLength, frontOfBridgeLength)

        # 다리에 트럭이 추가될 수 있는 경우
        if sum(curBridgeWeight) + truck <= weight and len(curBridgeWeight) < bridge_length:
            curBridgeWeight.append(truck)
            curBridgeLength.append(bridge_length)
            answer += 1

            # 한 칸씩 이동
            curBridgeLength = updateBridge(curBridgeLength, 1)
            # 다리를 다 건넌 트럭이 존재하는 경우
            if curBridgeLength and curBridgeLength[0] == 0:
                curBridgeLength.pop(0)
                curBridgeWeight.pop(0)

            print("case1 answer:", answer, "weight:", curBridgeWeight, "length:", curBridgeLength)

            continue

    if len(curBridgeLength) != 0:
        answer += curBridgeLength[-1]
    return answer