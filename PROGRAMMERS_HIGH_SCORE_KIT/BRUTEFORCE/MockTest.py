def solution(answers):
    answer = []
    answerCount = [0, 0, 0]
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for index, realAnswer in enumerate(answers):
        if student1[index % 5] == realAnswer:
            answerCount[0] += 1
        if student2[index % 8] == realAnswer:
            answerCount[1] += 1
        if student3[index % 10] == realAnswer:
            answerCount[2] += 1

    maxNum = max(answerCount)
    for index, count in enumerate(answerCount):
        if count == maxNum:
            answer.append(index + 1)
    return answer