from collections import deque 
def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False]*m for _ in range(n)]
    queue = deque([(0, 0)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    
    
    while queue:
        x, y = queue.popleft() 
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            
            if nx<0 or nx>n-1 or ny<0 or ny>m-1: 
                continue 
                
            if maps[nx][ny] == 0:
                continue 
                
            if not visited[nx][ny]:
                visited[nx][ny] = True
                maps[nx][ny] = maps[x][y] + 1 
                queue.append((nx, ny))
                
    answer = maps[n-1][m-1]
    return -1 if answer == 1 else answer