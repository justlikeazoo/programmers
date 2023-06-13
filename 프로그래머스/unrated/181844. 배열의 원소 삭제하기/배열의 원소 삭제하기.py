def solution(arr, delete_list):
    result = [x for x in arr if x not in delete_list]
    return result