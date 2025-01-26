def checkEnoughBrown(canW, canH, brown):
    needBrown = ((canW + 2) * 2) + (canH * 2)
    if needBrown == brown:
        return True
    return False


def solution(brown, yellow):
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            canW, canH = max(i, yellow // i), min(i, yellow // i)
            if checkEnoughBrown(canW, canH, brown):
                return [canW + 2, canH + 2]