def solution(s):
    answer = True
    i = 0
    for w in s:
        if w.lower() == 'p':
            i += 1 
        elif w.lower() == 'y':
            i -= 1 

    return i == 0