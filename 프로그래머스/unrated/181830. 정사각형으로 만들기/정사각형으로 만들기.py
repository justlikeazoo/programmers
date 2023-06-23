def solution(arr):
    row_count = len(arr)  # 행의 수
    col_count = len(arr[0])  # 열의 수
    
    # 행의 수가 더 많을 때
    if row_count > col_count:
        max_col_count = row_count  # 열의 수를 행의 수와 동일하게 설정
        
        for i in range(row_count):
            diff = max_col_count - len(arr[i])  # 추가할 0의 개수
            
            # 각 행의 끝에 0 추가
            arr[i] += [0] * diff
    
    # 열의 수가 더 많을 때
    elif row_count < col_count:
        max_row_count = col_count  # 행의 수를 열의 수와 동일하게 설정
        
        for i in range(row_count, max_row_count):
            # 새로운 행에 추가할 0으로 이루어진 리스트 생성
            new_row = [0] * col_count
            arr.append(new_row)
    
    return arr