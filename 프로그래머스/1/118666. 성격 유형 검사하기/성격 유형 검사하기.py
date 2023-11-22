def solution(survey, choices):
    dic_score = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    dic_result = {"R": 0, "T": 0, "C": 0, "F": 0, 
                  "J": 0, "M": 0, "A": 0, "N": 0} 
    mapping = {"R": 'T', "C": "F", "J": "M", "A": "N"}
    answer = ['R', 'C', 'J', 'A']
    
    for s, c in zip(survey, choices):
        if c > 4:
            dic_result[s[1]] += dic_score[c]    
        elif c < 4:
            dic_result[s[0]] += dic_score[c]
    
    for i in range(4):
        if dic_result[answer[i]] < dic_result[mapping[answer[i]]]:
            answer[i] = mapping[answer[i]]
    
    return "".join(answer)