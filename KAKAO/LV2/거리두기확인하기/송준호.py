from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                queue = deque()
                queue.append((i, j, 0))
                while queue:
                    x, y, dist = queue.popleft()
                    if dist < 2:
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if 0 <= nx < 5 and 0 <= ny <5 and place[nx][ny] != "X":
                                if place[nx][ny] == "P" and not (nx == i and ny == j):
                                    return False
                                else:
                                    queue.append((nx, ny, dist+1))
    return True

def solution(places):
    answer = []
    for place in places:
        if check(place):
            answer.append(1)
        else: answer.append(0)
    return answer
