def getMaxIndexOfInputNumber(number, citations):
    '''
    :param number: 기준이 되는 숫자
    :param citations: 정렬된 citations
    :return: citations에서 값이 number를 넘지 않으면서 가장 큰 숫자의 index 값
    '''
    index = 0;
    for i in range(len(citations)):
        if citations[i] < number:
            continue
        if (citations[i] >= number):
            index = i;
            break

    return index;


def solution(citations):
    """
    :param citations: 과학자가 발표한 논문의 인용 횟수를 담은 배열
    :return:과학자의 H-Index
    """
    answer = 0

    # citations을 오름차순으로 정렬
    citations.sort()

    # citation의 max값 + 1 까지 for문을 수행
    for h in range(citations[-1] + 1):
        # citations에서 h값보다 큰 값의 개수를 센 후, 그 개수가 h 보다 크다면 answer에 저장
        numberOfMoreThanH = len(citations) - getMaxIndexOfInputNumber(h, citations)
        if (numberOfMoreThanH >= h):
            answer = h

    return answer
