language = {"python": [], "java": [], "cpp": []}
career = {'senior': [], "junior": []}
soulfood = {'chicken': [], 'pizza': []}
career_type = {'frontend': [], 'backend': []}
all = []
score = []

def solution(info, query):
    answer = []
    for i, info_iter in enumerate(info):
        lan, car_type, car, soul, sc = info_iter.split()
        language[lan].append(i)
        career_type[car_type].append(i)
        career[car].append(i)
        soulfood[soul].append(i)
        all.append(i)
        score.append(sc)
    
    for query_iter in query:
        q = query_iter.split(" and ")
        q += q.pop().split()
        lan, car_type, car, soul, sc = q
        temp_set = set(all)
        if lan == "-":
            temp_set = temp_set & set(all)
        else: 
            temp_set = temp_set & set(language[lan])
        if car_type == "-":
            temp_set = temp_set & set(all)
        else: 
            temp_set = temp_set & set(career_type[car_type])
        if car == "-":
            temp_set = temp_set & set(all)
        else: 
            temp_set = temp_set & set(career[car])
        if soul == "-":
            temp_set = temp_set & set(all)
        else: 
            temp_set = temp_set & set(soulfood[soul])
            
        temp_set = list(temp_set)
        count = 0
        while temp_set:
            if int(sc) <= int(score[temp_set.pop()]):                
                count += 1

        answer.append(count)
    
    return answer