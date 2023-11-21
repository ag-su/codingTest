def solution(s):
    answer = []
    lst_s = [list(map(int, s1.split(','))) for s1 in s[2:-2].split("},{")]
    
    lst_s.sort(key=lambda x: len(x))
    
    set_prev = set()
    for i, nums in enumerate(lst_s):
        set_nums = set(nums)
        
        
        cur = set_nums - set_prev
        answer.append(list(cur)[0])

        set_prev = set_nums
        
    return answer
