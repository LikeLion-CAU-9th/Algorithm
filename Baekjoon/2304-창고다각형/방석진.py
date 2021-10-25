N = int(input())

coord_dict = dict()

for _ in range(N):
    key, value = map(int, input().split())
    coord_dict[key] = value

sorted_coord = sorted(coord_dict.items(), key = lambda x : x[1])

initial_x, initial_y = sorted_coord.pop()
left_x = initial_x; right_x = initial_x; answer = 0
answer += initial_y

for x, y in reversed(sorted_coord):
    if right_x < x: 
        answer += (x - right_x) * y
        right_x = x
    if left_x > x:
        answer += (left_x - x) * y
        left_x = x

print(answer)
    