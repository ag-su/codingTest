def solution(N, stages):
    answer = [] 
    challenger = len(stages)
    for i in range(1, N+1): 
        
        fail = stages.count(i) # 스테이지 i를 실패한 사람 수 
        
        if fail == 0: answer.append((i, 0)) # 실패한 사람이 없으면 0 추가
        else: answer.append((i, fail/challenger)) 
        challenger -= fail # 이번 스테이지에 실패한 사람은 다음 스테이지 도전자가 아니므로.
                               
    answer.sort(key=lambda x: x[1], reverse=True)
    
    return [i for i, v in answer]