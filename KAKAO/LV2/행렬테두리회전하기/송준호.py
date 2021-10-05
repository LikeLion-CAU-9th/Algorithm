def 둥글게둥글게(board, x1, y1, x2, y2):
    start = board[x1][y1]
    x, y = x1, y1
    min_value = start
    while x < x2:
        board[x][y] = board[x+1][y]
        min_value = min(min_value, board[x][y])
        x += 1
    while y < y2:
        board[x][y] = board[x][y+1]
        min_value = min(min_value, board[x][y])
        y += 1
    while x > x1:
        board[x][y] = board[x-1][y]
        min_value = min(min_value, board[x][y])
        x -= 1
    while y > y1:
        board[x][y] = board[x][y-1]
        min_value = min(min_value, board[x][y])
        y -= 1
    board[x][y+1] = start

    return board, min_value


def solution(rows, columns, queries):
    board = [[0]*columns] + [[0]+list(range(i*columns+1, (i+1)*columns+1)) for i in range(rows)] # 제일 왼쪽 위 좌표가 (1,1)이 되도록 0번째 줄을 추가했습니당
    answer = []
    for query in queries:
        board, min_value = 둥글게둥글게(board, *query)
        answer.append(min_value)
    return answer
