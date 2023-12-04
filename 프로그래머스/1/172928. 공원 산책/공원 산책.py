def solution(park, routes):
    dic_moves = {
        "N": (-1, 0),
        "S": (1, 0),
        "W": (0, -1),
        "E": (0, 1)
    }
    
    l, k = len(park), len(park[0])
    
    x, y = 0, 0 
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "S":
                x, y = i, j
                break 
        
    for r in routes: 
        d, n = r.split()
        n = int(n)
        dx, dy = dic_moves[d]
            
        for i in range(1, n+1):
            nx, ny = x+dx*i, y+dy*i
            if nx<0 or nx>l-1 or ny<0 or ny>k-1: 
                break 
                
            if park[nx][ny] == "X": 
                break 
                
        else:
            x, y = nx, ny 
        
    return [x, y]