def solution(n, from_p, to_p, aux_p):
    if n==1:
        print(from_p,',',to_p)
        return
    solution(n-1, from_p, aux_p, to_p)
    print(from_p, ',', to_p)
    solution(n-1, aux_p, to_p, from_p)

print(2**3-1)
solution(3,1,3,2)
