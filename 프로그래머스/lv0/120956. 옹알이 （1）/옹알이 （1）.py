def solution(babbling):
    answer = 0 
    for b in babbling: 
        s = ""
        for c in b: 
            s += c 
            if s in ["aya", "ye", "woo", "ma"]: 
                s = ""
        if len(s) == 0: 
            answer += 1 

            
    return answer