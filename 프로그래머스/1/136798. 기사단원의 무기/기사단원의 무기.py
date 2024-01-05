import math
def solution(number, limit, power):    
    # 기사 번호의 약수 개수에 해당하는 공격력을 가진 무기 구매 
    # 공격력 제한 수치 있음. => 더 크면 정해진 공격력 무기 구매 
    answer = 0
    for i in range(1, number+1):
        cnt = 0 
        for j in range(1, int(math.sqrt(i))+1):
            if i/j == math.sqrt(i):
                cnt += 1 
            elif i % j == 0:
                cnt += 2 
        if cnt > limit:
            answer += power
        else:
            answer += cnt
    
    return answer