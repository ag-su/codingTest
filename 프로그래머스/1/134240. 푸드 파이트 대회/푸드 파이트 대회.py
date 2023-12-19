def solution(food):
    temp = []
    for i, n in enumerate(food):
        if i == 0:
            continue 
        temp += [f"{i}"] * (n//2)
        
    answer = temp + ["0"] + list(reversed(temp))
        
    return "".join(answer)