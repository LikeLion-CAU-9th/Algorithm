N = int(input())
schedule = []
for _ in range(N):
    T, P = map(int, input().split())
    schedule.append((T, P))

dp = [0]*(N+1) #dp[k] = k번째 날이 끝난 후 최대수익
for i in range(N):
    T, P = schedule[i]
    end = i + T #end: i+1번째 스케쥴이 끝나는 날 
    if end <= N:
        dp[end] = max(dp[end], dp[i] + P)
    dp[i+1] = max(dp[i], dp[i+1])

print(dp[N])
