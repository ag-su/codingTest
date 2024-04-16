def solution(n):
    answer = 0
    t = n//2 + n%2
    while t >= 2:
        s = t
        for i in range(t-1, 0, -1):
            s += i
            if s > n:
                break
            elif s == n:
                answer += 1
                break
        else:
            break
            
        t -= 1 

    return answer + 1 