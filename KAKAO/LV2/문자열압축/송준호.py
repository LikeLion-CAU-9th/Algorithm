def solution(s):
    length = len(s)
    answer = length
    for unit_size in range(1, length//2+1):
        compressed_length = 0
        units = int(length // unit_size)
        temp = [] * unit_size
        count = 0
        for i in range(units):
            cur_unit = s[i*unit_size:(i+1)*unit_size]
            if temp == cur_unit:
                count += 1
                if count == 2 or count == 10 or count == 100 or count == 1000:
                    compressed_length += 1
            else:
                temp = cur_unit
                count = 1
                compressed_length += unit_size
        compressed_length += length % unit_size
        answer = min(answer, compressed_length)
    return answer
