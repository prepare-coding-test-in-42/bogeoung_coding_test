def solution(progresses, speeds):
    answer = [1]
    totalNeedDays = []

    for progress, speed in zip(progresses, speeds):
        # 필요 일수 계산
        remainDays = 100 - progress
        needDays = remainDays // speed
        if (remainDays % speed) != 0:
            needDays += 1

        # 선행 배포가 완료되었는지 확인
        if (totalNeedDays and (totalNeedDays[-1] > needDays)):
            totalNeedDays.append(totalNeedDays[-1])
        else:
            totalNeedDays.append(needDays)

    for idx in range(1, len(totalNeedDays)):
        if totalNeedDays[idx] == totalNeedDays[idx - 1]:
            answer[-1] += 1
        else:
            answer.append(1)

    return answer