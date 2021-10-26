from itertools import permutations

orders = list(permutations(["+","-","*"], 3))

def solution(expression):
    answer = 0
    items = []
    temp = ""
    for char in expression:
        try:
            temp += str(int(char))
        except:
            items.append(int(temp))
            items.append(char)
            temp = ""
    items.append(int(temp))

    for i in range(6):
        order = orders[i]
        temp_items = items[:]
        for sign in order:
            k = 0
            for i in range(len(temp_items)):
                if temp_items[i-k] == sign:
                    if sign == "+":
                        result = temp_items[i-k-1] + temp_items[i-k+1]
                    elif sign == "-":
                        result = temp_items[i-k-1] - temp_items[i-k+1]
                    elif sign == "*":
                        result = temp_items[i-k-1] * temp_items[i-k+1]
                    for _ in range(3):
                        del temp_items[i-k-1]
                    temp_items.insert(i-k-1, result)
                    k += 2
        answer = max(answer, abs(temp_items[0]))

    return answer
