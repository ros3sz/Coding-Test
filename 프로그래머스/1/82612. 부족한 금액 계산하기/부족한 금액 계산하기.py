def solution(price, money, count):
    answer = -1
    cost = sum((c * price) for c in range(count+1))
    if cost >= money :
        answer = cost - money
    else :
        answer = 0

    return answer