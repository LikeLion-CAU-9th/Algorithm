n = int(input("자연수를 입력하세요."))

def hanoi_tower(n, start_col, end_col, middle_col):
    if n == 1:
        print(start_col, end_col)
        return
    else:
        hanoi_tower(n-1 , start_col, middle_col, end_col)
    print(start_col, end_col)
    hanoi_tower(n-1, middle_col, end_col, start_col)

    


hanoi_tower(n,1,3,2)
print((2 ** n)-1)

''' reculsive relation은 잘 이해가 되었으나, 이를 reculsion을 이용한 code로 표현하는 것이 어려웠다.
기둥 3개를 변수로 받을 생각도 하지 못했다. '''