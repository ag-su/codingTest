N, M = map(int, input().split())
nums = list(map(int, input().split()))

# 누적합 배열 구하기 
arr = [nums[0] % M] 
for i in range(1, N): 
    arr.append((arr[i-1] + nums[i]))
    

# 개수 배열 구하기 
arr_cnt = [0] * M
for n in arr: 
    arr_cnt[n%M] += 1 

result = arr_cnt[0] 

for cnt in arr_cnt: 
    if cnt >= 2: 
        result += ((cnt * (cnt-1)) // 2)
        
print(result)