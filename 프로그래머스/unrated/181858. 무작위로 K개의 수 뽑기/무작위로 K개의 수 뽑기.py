def solution(arr, k):
    result = []  # 완성될 배열
    unique_nums = set()  # 지금까지 나온 수를 저장할 집합

    for num in arr:
        if num not in unique_nums:  # 지금까지 나온 적 없는 수인 경우
            unique_nums.add(num)  # 수를 집합에 추가
            result.append(num)  # 배열 맨 뒤에 추가

            if len(result) == k:  # 완성될 배열의 길이가 k와 같으면 반복 종료
                break

    if len(result) < k:
        result.extend([-1] * (k - len(result)))  # 나머지 값을 -1로 채움

    return result