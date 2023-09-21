def solution(my_string):
    answer = sorted([my_string[-i:] for i in range(len(my_string))])
    # sort : 원본을 정렬하고 수정합니다 (in-place)
    # sorted : 원본은 유지하고 정렬한 새 리스트를 만듭니다.
    return answer