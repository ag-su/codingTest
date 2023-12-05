def solution(s):
    answer = 0
    a, b = 0, 0
    cur = ""
    for string in s:
        if a == 0:
            cur = string
        if string == cur:
            a += 1 
        else:
            b += 1
        if a == b:
            answer += 1 
            a, b = 0, 0
    if a != 0:
        answer += 1 
    return answer