def solution(k, m, score):
    answer = 0
    # m: 한 상자에 들어있는 사과 개수 
    # k: 가장 큰 점수 
    # p: 가장 낮은 점수 
    # 사과 한 상자의 가격: p * m 
    
    score.sort(reverse=True) 
    
    for i in range(len(score)//m): 
        answer += score[m*i+m-1] * m
    
    
    return answer