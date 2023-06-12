import sys 
input = sys.stdin.readline

N, M = map(int, input().split())

lst_origin = [[0] * (N+1)]
lst_new = [[0] * (N+1) for _ in range(N+1)]

# 입력 받은 배열
for i in range(N): 
    lst_rows = [0] + list(map(int, (input().split())))
    lst_origin.append(lst_rows)

# 구간합 배열 생성  
for i in range(1, N+1):
    for j in range(1, N+1):
        lst_new[i][j] += lst_origin[i][j] + lst_new[i-1][j] + lst_new[i][j-1] - lst_new[i-1][j-1]  

# 질의 입력 및 응답 출력
for _ in range(M): 
    x1, y1, x2, y2 = map(int, (input().split()))
    result = lst_new[x2][y2] - lst_new[x1-1][y2] - lst_new[x2][y1-1] + lst_new[x1-1][y1-1]
    print(result)