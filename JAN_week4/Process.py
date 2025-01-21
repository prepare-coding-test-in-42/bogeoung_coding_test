def solution(priorities, location):
    curProcessOrder = 0

    while True:
        maxPriority = max(priorities)
        curPriority = priorities.pop(0)
        # 우선순위가 제일 높은지 확인
        if curPriority == maxPriority:
            curProcessOrder += 1
            # 찾으려던 프로세스인 경우
            if location == 0:
                return curProcessOrder
            # 그렇지 않은 경우
            if location > 0:
                location -= 1
        # 우선순위가 제일 높지 않다면 제일 후순위로 미룸
        if curPriority != maxPriority:
            priorities.append(curPriority)
            if location == 0:
                location = len(priorities)
            if location > 0:
                location -= 1

    return curProcessOrder