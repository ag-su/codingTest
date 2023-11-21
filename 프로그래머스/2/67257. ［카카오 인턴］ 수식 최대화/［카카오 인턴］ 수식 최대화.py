import re 
def calc(n1, n2, operator):
    n1, n2 = int(n1), int(n2)
    if operator == "+":
        return n1 + n2
    elif operator == "-":
        return n1 - n2
    elif operator == "*":
        return n1 * n2 

def solution(expression):
    answer = 0
    split_ex = re.split(r'([-+*])', expression)
    lst_operand = [int(s) for s in split_ex if s.isdigit()]
    lst_operator = [s for s in split_ex if not s.isdigit()]
    lst_o = ["+ - *", "+ * -", "- + *", "- * +", "* + -", "* - +"]
    
    for str_o in lst_o:
        lst_tmp = split_ex.copy() 
        for o in str_o.split():
            for _ in range(lst_operator.count(o)):
                for i, c in enumerate(lst_tmp): 
                    if c == o:
                        result = calc(lst_tmp[i-1], lst_tmp[i+1], c)
                        lst_tmp[i] = result
                        del lst_tmp[i-1], lst_tmp[i]
                        break
                        
        if answer < abs(int(lst_tmp[0])):
            answer = abs(int(lst_tmp[0]))
                    
    return answer
