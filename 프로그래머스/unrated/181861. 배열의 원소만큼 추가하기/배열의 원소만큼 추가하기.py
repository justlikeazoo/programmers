def solution(arr):
    result = []
    
    for num in arr:
        result += [num] * num
    
    return result