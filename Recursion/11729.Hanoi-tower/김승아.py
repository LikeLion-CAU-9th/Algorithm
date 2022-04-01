import sys

def solve(a, b, c, n):
    if n == 1: #최소 이동횟수
        print(a, c)
    else:
        solve(a, c, b, n - 1)
        print(a, c)
        solve(b, a, c, n - 1)

n = int(sys.stdin.readline())
print(2**n - 1)
solve(1, 2, 3, n)
