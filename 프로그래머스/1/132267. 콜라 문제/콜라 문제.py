def solution(a, b, n):
    answer = 0
    
    while n >= a:
        get = (n // a) * b
        remain = n % a 
        answer += get
        n = get + remain
        
    return answer