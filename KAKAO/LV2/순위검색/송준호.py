import bisect

def solution(info, query):
    answer = []
    applicants = [[[[[] for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(4)]
    for applicant in info:
        lang, group, career, food, score = applicant.split()
        if lang == "cpp":
            lang = 1
        elif lang == "java":
            lang = 2
        else: lang = 3
        if group == "backend":
            group = 1
        else: group = 2
        if career == "junior":
            career = 1
        else: career = 2
        if food == "chicken":
            food = 1
        else: food = 2
        score = int(score)
        """
        applicants 배열은 지원자들을 각 속성별로 분류하여 이에 속하는 지원자들의 점수를 모아놓은 배열이다.
        applicants[1][1][1][1]에는 cpp사용하는 백엔드 주니어 개발자면서 치킨을 좋아하는 지원자들의 점수들이 담겨있다.
        applicants[1][1][1][0]처럼 index가 0인 경우는 해당 속성이 상관 없는 경우이다.
        즉 위 경우는 cpp사용하는 백엔드 주니어 개발자인 지원자(음식은 노상관)들의 점수를 모아놓은 배열이다.

        따라서 cpp사용하는 백엔드 주니어 개발자면서 치킨을 좋아하는 지원자의 점수는,
        applicants[0 or 1][0 or 1][0 or 1][0 or 1] 이렇게 총 16개 배열에 들어간다.
        """
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    for l in range(2):
                        applicants[i*lang][j*group][k*career][l*food].append(score)
    for i in range(4): #점수컷을 만족하는 지원자 수를 빠르게 세기 위해 점수들을 정렬해둔다.
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        applicants[i][j][k][l].sort()

    for filter in query:
        count = 0
        filter_list = filter.split()
        if filter_list[0] == "cpp":
            lang = 1
        elif filter_list[0] == "java":
            lang = 2
        elif filter_list[0] == "python":
            lang = 3
        else: lang = 0
        if filter_list[2] == "backend":
            group = 1
        elif filter_list[2] == "frontend":
            group = 2
        else: group = 0
        if filter_list[4] == "junior":
            career = 1
        elif filter_list[4] == "senior":
            career = 2
        else: career = 0
        if filter_list[6] == "chicken":
            food = 1
        elif filter_list[6] == "pizza":
            food = 2
        else: food = 0
        score = int(filter_list[7])
        # 해당 조건을 만족하는 지원자들의 점수들에서 점수컷이 위치하는 인덱스를 이분탐색으로 확인한다. (그냥 탐색해도 될 듯?)
        count = len(applicants[lang][group][career][food]) - bisect.bisect_left(applicants[lang][group][career][food],score)
        answer.append(count)

    return answer
