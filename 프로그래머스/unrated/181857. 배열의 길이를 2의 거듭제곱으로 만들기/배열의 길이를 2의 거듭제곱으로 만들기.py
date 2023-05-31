def solution(arr):
    n = len(arr)
    target_length = 1

    while target_length < n:
        target_length *= 2

    if target_length > n:
        arr.extend([0] * (target_length - n))

    return arr