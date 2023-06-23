def solution(arr):
    n = len(arr)  # 이차원 배열의 크기
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] != arr[j][i]:
                return 0  # 조건을 만족하지 않으면 0을 반환
    
    return 1  # 모든 요소가 조건을 만족하면 1을 반환