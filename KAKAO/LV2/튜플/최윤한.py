inputstr = input("string")
a = inputstr.replace('{','').replace('}','')
b = a.split(',')
numbers = set(b) # list를 집합으로 저장하면서, 자동으로 중복된 숫자들은 하나로 처리한다.

result = []
for i in numbers:
    result.append(int(i))

print (result)
