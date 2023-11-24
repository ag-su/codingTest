def to_days(date):
    year, month, day = list(map(int, date.split(".")))
    return (year*12*28) + (month*28) + day
    
    
def solution(today, terms, privacies):
    answer = [] 
    
    today = to_days(today) # 오늘 일 수
    dic_terms = {t[0]:int(t[2:])*28 for t in terms} # 약관 딕셔너리
    
    for i, privacy in enumerate(privacies):
        date, term = privacy.split() 
        
        if to_days(date) + dic_terms[term] <= today:
            answer.append(i+1)

    return answer