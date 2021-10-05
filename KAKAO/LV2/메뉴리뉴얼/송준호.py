from itertools import combinations

def solution(orders, course):
    answer = []
    for i in range(len(orders)):
        orders[i] = "".join(sorted(list(orders[i]))) #3번 TC처럼 오더가 정렬되어있지 않으면 XW와 WX가 따로 계산되므로 정렬해줬음
    for N in course:
        counter = dict()
        for order in orders:
            for combo in combinations(order, N):
                if combo in counter.keys():
                    counter[combo] += 1
                else:
                    counter[combo] = 1

        max_value = 0
        if counter: #가능한 콤보가 없는 경우 걸러줌
            max_value = max(counter.values())
        if max_value >= 2: #2번 이상 주문되었어야 함
            for combo in counter:
                if counter[combo] == max_value:
                    answer.append("".join(combo))
    answer.sort()
    return answer
