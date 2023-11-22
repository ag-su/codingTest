def solution(n, arr1, arr2):
    answer = []
    
    for a1, a2 in zip(arr1, arr2):
        b = bin(a1 | a2)[2:]
        b = "0"*(n-len(b)) + b
        answer.append(b.replace("1", "#").replace("0", " "))

    return answer