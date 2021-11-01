N = int(input())
pillars = []
max_height = 0 #최고기둥높이
for _ in range(N):
    x, height = map(int, input().split())
    pillars.append((x, height))
    max_height = max(max_height, height)

pillars.sort()
answer = max_height #최고높이의 기둥의 높이 우선 더함
height = 0 
x = 1001

while height != max_height: #최고높이의 기둥으로부터 오른쪽부분 해결 
    cur_x, cur_h = pillars.pop()
    if cur_h >= height:
        answer += height * (x - cur_x)
        x = cur_x
        height = cur_h

pillars.append((x, height))
max_x = x
height = 0
x = 0
pillars.sort(reverse=True) 
while pillars: #최고높이의 기둥으로부터 왼쪽부분 해결
    cur_x, cur_h = pillars.pop()
    if cur_h >= height:
        answer += height * (cur_x - x)
        x = cur_x
        height = cur_h

print(answer)
