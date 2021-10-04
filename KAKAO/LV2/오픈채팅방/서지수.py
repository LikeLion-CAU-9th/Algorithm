def solution(record):
    dic={}
    for i in range(len(record)):
        order=record[i].split(' ')
        if order[0]=="Enter":
            dic[order[1]]=order[2]
        elif order[0]=="Change":
            del dic[order[1]]
            dic[order[1]]=order[2]
    
    #dic에서 result만들기
    result=[]
    for i in range(len(record)):
        order=record[i].split(' ')
        if order[0]=="Enter":
            result.append(dic[order[1]]+"님이 들어왔습니다.")
        elif order[0]=="Leave":
            result.append(dic[order[1]]+"님이 나갔습니다.")
    
    print(result)

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
