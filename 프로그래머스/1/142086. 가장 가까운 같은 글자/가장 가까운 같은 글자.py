def solution(s):
    dic = {}
    answer = [0] * len(s)
    for i, string in enumerate(s):
        if string not in dic.keys():
            dic[string] = i
            answer[i] = -1
            continue
        answer[i] = i - dic[string]
        dic[string] = i
    
    return answer