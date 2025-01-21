from collections import Counter
def solution(participant, completion):
    participantCounter = Counter(participant)
    completionCounter = Counter(completion)
    answerCounter = participantCounter - completionCounter

    for key, value in answerCounter.items():
        return key

