def solution(numbers, target):
    answer = recur(numbers, target, 0)
    return answer

def recur(numbers, target, i):
    answer = 0
    if i == len(numbers):
        if sum(numbers) == target:
            return 1
        else: 
            return 0
    else:
        answer += recur(numbers, target, i+1)
        numbers[i] *= -1
        answer += recur(numbers, target, i+1)
        return answer
