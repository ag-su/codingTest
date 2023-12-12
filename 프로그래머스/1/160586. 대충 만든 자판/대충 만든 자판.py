def solution(keymap, targets):
    dic_cnt = {}  
    
    for key in keymap: 
        for i, k in enumerate(key): 
            if (k in dic_cnt.keys()) and (i+1 >= dic_cnt[k]):
                 continue
            dic_cnt[k] = i+1 
                
    answer = [0] * len(targets)
    for i, target in enumerate(targets):
        for t in target:
            if t not in dic_cnt.keys():
                answer[i] = -1 
                break 
            answer[i] += dic_cnt[t]
    
    return answer
