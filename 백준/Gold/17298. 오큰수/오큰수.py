N = int(input())
lst_nums = list(map(int, input().split()))


# 스택: 인덱스를 넣어줌 
stack = [] 

# 결과 리스트: 오큰수를 넣어줌 
results = [-1] * N

for i in range(N):      
    # => stack에 남아있는 조건에 해당하는 수만큼 반복함
    current = lst_nums[i]
    # 스택에 값이 있음 & current > stack TOP 일 동안 반복
    while stack and (current > lst_nums[stack[-1]]):
        # stack TOP pop  
        nge_idx = stack.pop()

        # results의 pop index에 current 저장
        results[nge_idx] = current
                                    
    # stack append
    stack.append(i)
    
for n in results: 
    print(n, end=' ')