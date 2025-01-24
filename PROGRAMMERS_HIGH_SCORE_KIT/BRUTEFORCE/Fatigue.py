from itertools import permutations

def solution(k, dungeons):
    answer = -1

    numList = []
    permList = []
    for i in range(0, len(dungeons)):
        numList.append(i)
        permList.append([i])

    for i in range(2, len(dungeons) + 1):
        perm = permutations(numList, i)
        for p in perm:
            permList.append(list(p))

    for perm in permList:
        tempK = k
        tempAnswer = 0
        for index in perm:
            dungeon = dungeons[index]
            if tempK >= dungeon[0]:
                tempK -= dungeon[1]
                tempAnswer += 1
            elif tempK < dungeon[0]:
                break
        answer = max(answer, tempAnswer)
    return answer