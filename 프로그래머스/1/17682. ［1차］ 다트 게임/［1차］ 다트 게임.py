def solution(dartResult):
    answer = []
    # 제곱: S: 1, D: 2, T: 3  
    # 옵션: *: 해당 점수, 바로 전 점수 2배, #: 해당 점수 마이너스  
    
    dic_str2num = {"S":1, "D":2, "T":3, "*": 2, "#": -1}
    current = 0
    i = 0
    for idx, s in enumerate(dartResult):
        if s.isdigit(): 
            if s=="1" and dartResult[idx+1]=="0":
                current = 10
                i += 1
            elif s=="0" and dartResult[idx-1]=="1":
                continue
            else:
                current = int(s)
                i += 1 
        
        elif s in "SDT":
            result = current ** dic_str2num[s]
            answer.append(result) 
            
        else:
            if (s == "*") and (i > 1):
                answer[i-2] = answer[i-2] * dic_str2num[s]    
            answer[i-1] = answer[i-1] * dic_str2num[s] 
        
        
    return sum(answer)