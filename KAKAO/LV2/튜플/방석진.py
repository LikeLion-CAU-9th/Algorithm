def solution(s):
    s = bracket_remover(s)
    s_list = s.split("},")
    s_list = [bracket_remover(iter).split(",") for iter in s_list]
    s_list = sorted(s_list, key= lambda x : len(x))

    answer = list(); temp = list()

    for iter in s_list: 
        for i in iter:
            if i not in temp:
                answer.append(int(i))
        temp = iter
        
    return answer

def bracket_remover(s):
    if s[0] == "{" and s[-1] == "}":
        return s[1:-1]
    elif s[0] == "{": 
        return s[1:]
    elif s[0] == "}":
        return s[:-1]