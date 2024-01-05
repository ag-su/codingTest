def solution(X, Y):
    answer = ""
    
    X, Y = list(X), list(Y)
    X.sort(reverse=True)
    Y.sort(reverse=True) 
    
    i, j = 0, 0 
    while i < len(X) and j < len(Y): 
        if X[i] < Y[j]: 
            j += 1 
        elif X[i] > Y[j]: 
            i += 1 
        else: 
            answer += X[i]
            i += 1 
            j += 1 
    
    if len(answer) == 0: 
        answer = "-1" 
    elif answer[0] == "0":
        answer = "0" 

        
    return answer