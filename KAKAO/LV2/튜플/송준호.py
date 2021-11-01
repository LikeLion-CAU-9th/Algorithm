def solution(s):
    answer = []
    counter = dict()
    temp = ""
    s = list(s[::-1])
    while s:
        char = s.pop()
        if char.isdigit():
            temp += char
        else:
            if temp:
                num = int(temp)
                if num in counter:
                    counter[num] += 1
                else:
                    counter[num] = 1
            temp = ""
    answer = sorted(list(counter.keys()), key = lambda x:-counter[x])
    return answer
