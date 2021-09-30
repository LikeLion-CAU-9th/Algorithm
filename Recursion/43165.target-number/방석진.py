count = 0
def solution(numbers, target):
    global count
    recur(target, len(numbers) - 1, numbers)
    return count 

def recur(result, idx, numbers):
    global count
    if idx == 0:
        if abs(result) == numbers[0]:
            count += 1
        return 
    
    recur(result - numbers[idx], idx - 1, numbers)
    recur(result + numbers[idx], idx - 1, numbers)