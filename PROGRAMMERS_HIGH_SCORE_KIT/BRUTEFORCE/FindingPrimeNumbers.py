from itertools import permutations
import math

def isPrimeNumber(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    numList = list()

    for number in numbers:
        numList.append(number)

    permIters = set()
    for i in range(len(numList)):
        permIter = permutations(numList, i + 1)
        for perm in permIter:
            permIters.add(int(''.join(perm)))

    if 1 in permIters:
        permIters.remove(1)
    if 0 in permIters:
        permIters.remove(0)

    for perm in permIters:
        if isPrimeNumber(perm):
            answer += 1
    return answer