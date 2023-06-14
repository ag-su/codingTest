from collections import deque 

N, L = map(int, input().split())
lst_nums = list(map(int, input().split()))

mydeque = deque() 

for i in range(N): 
    while mydeque and mydeque[-1][0] > lst_nums[i]:
        mydeque.pop() 
    mydeque.append((lst_nums[i], i))
    
    if mydeque[-1][1] - mydeque[0][1] >= L: 
        mydeque.popleft() 
    
    print(mydeque[0][0], end=' ')