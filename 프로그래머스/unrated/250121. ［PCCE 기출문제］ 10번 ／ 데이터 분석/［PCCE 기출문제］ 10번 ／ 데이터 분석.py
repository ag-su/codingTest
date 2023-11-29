def solution(data, ext, val_ext, sort_by):
    answer = []
    dic_ext = {"code":0, "date":1, "maximum":2, "remain":3}
    for d in data:
        if d[dic_ext[ext]] < val_ext:
            answer.append(d)
    
    return sorted(answer, key=lambda x: x[dic_ext[sort_by]])