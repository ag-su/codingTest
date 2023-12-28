from collections import deque 
def solution(k, score):
    answer = [score[0]]
    queue = deque([score[0]])
    
    for s in score[1:]:
        queue.append(s)
        i = len(queue)-1
        while i > 0:
            if queue[i-1] <= queue[i]:
                break
            elif queue[i-1] > queue[i]:
                queue[i-1], queue[i] = queue[i], queue[i-1]
                i -= 1 
                
        if len(queue) > k:
            queue.popleft()
    
        answer.append(queue[0])
        
    return answer