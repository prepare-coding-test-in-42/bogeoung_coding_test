def solution(s):
    stack = []

    for bracket in s:
        if bracket == "(":
            stack.append("(")
        if bracket == ")" and len(stack) == 0:
            return False
        if bracket == ")" and len(stack) > 0:
            stack.pop()

    if len(stack) > 0:
        return False

    return True