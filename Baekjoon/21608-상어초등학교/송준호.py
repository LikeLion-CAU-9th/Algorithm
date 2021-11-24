N = int(input())
board = [[0]*N for _ in range(N)]
loves = [[] for _ in range((N**2)+1)] #좋아하는 사람 리스트

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N**2):
    man, *cur_loves = map(int, input().split())
    loves[man] = cur_loves
    love, blank, row, col = -1, 0, 0, 0
    for x in range(N):
        for y in range(N): #왼쪽 위칸부터 평가 시작
            if board[x][y] == 0: #칸이 비어있다면
                cur_love = 0
                cur_blank = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < N:
                        if board[nx][ny] == 0: #주변 빈칸 갯수 세기
                            cur_blank += 1
                        if board[nx][ny] in cur_loves: #주변 좋아하는 사람 수 세기
                            cur_love += 1
                if cur_love > love: #주변 좋아하는 사람 수가 최대라면
                    love, blank, row, col = cur_love, cur_blank, x, y #현재자리 기록
                elif cur_love == love:
                    if cur_blank > blank: #주변 좋아하는 사람 수는 동점인데 주변 빈칸은 더 많다면
                        love, blank, row, col = cur_love, cur_blank, x, y #현재자리 기록
    board[row][col] = man #최고 만족도 자리를 기록

answer = 0
for x in range(N):
    for y in range(N):
        man = board[x][y]
        count = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] in loves[man]:
                count += 1
        if count > 0:
            answer += 10**(count-1)

print(answer)
