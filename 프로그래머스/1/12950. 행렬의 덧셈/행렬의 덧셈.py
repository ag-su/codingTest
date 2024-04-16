def solution(arr1, arr2):
    answer = []
    for l1, l2 in zip(arr1, arr2): 
        answer.append([l1[i] + l2[i] for i in range(len(l1))]) 
            
    return answer