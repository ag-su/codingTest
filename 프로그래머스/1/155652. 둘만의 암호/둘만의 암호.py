def solution(s, skip, index):
    
    alphas = sorted(set("abcdefghijklmnopqrstuvwxyz") - set(skip))
    answer = ''
    
    for char in s: 
        new_idx = (alphas.index(char) + index) % len(alphas) 
        answer += alphas[new_idx]
        
    return answer