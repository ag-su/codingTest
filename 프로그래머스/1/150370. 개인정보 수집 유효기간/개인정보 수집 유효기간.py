def solution(today, terms, privacies):
    answer = []
    dic_terms = {t.split()[0]:int(t.split()[1])  for t in terms}
    
    for i, p in enumerate(privacies): 
        term = p.split()[1] # 약관 
        year, month, day = list(map(int, p.split()[0].split("."))) # 날짜 분리 
        month = month + dic_terms[term] # 유효기간 계산 
        day -= 1  
    
        if month > 12:
            if month%12 == 0:
                year += month//12-1
            else: 
                year += month//12
            month = month%12

        if day == 0:
            month -= 1
            day = 28
            if month == 1:
                year -= 1   
                
        if month == 0:
            month = 12 
        
        print(year, month, day)
        
        if today > f"{year}.{str(month).zfill(2)}.{str(day).zfill(2)}":
            answer.append(i+1)
            

    return answer