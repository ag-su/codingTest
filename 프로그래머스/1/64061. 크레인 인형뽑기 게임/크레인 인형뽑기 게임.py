def solution(board, moves):
    result = 0
    stack = []
    for m in moves: 
        for i in range(len(board)):
            if board[i][m-1] !=0:
                item = board[i][m-1]
                
                board[i][m-1] = 0
                
                if stack and (stack[-1] == item):
                    stack.pop()
                    result += 2
                    break
                else:
                    stack.append(item)
                    break

    return result