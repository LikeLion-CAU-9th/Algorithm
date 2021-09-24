import sys

N = int(sys.stdin.readline())

def hanoi(n, start, end, via):
    if n == 1:
        print("{} {}".format(start, end))
    else:
        hanoi(n - 1, start, via, end)
        print("{} {}".format(start, end))
        hanoi(n - 1, via, end, start)
    
count = 0
for _ in range(N):
    count += count + 1
else: print(count)

hanoi(N, 1, 3, 2)