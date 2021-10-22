def is_valid(p):
    count = 0
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    if count == 0:
        return True
    else:
        return False


def reverse(p):
    reversed_p = ""
    for i in range(len(p)):
        if p[i] == "(":
            reversed_p += ")"
        else:
            reversed_p += "("
    return reversed_p


def solution(p):
    if p == "":
        return ""
    if is_valid(p):
        return p
    N = len(p)
    count = 0
    divider = 0
    for i in range(N):
        if p[i] == "(":
            count += 1
        else: count -=1
        if count == 0:
            divider = i+1
            break
    u = p[:divider]
    v = p[divider:]
    if is_valid(u):
        return u + solution(v)
    else:
        return "(" + solution(v) + ")" + reverse(u[1:-1])
