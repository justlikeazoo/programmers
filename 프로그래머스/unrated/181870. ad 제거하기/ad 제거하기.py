def solution(strArr):
    result = []
    for string in strArr:
        if "ad" not in string:  # "ad"를 포함하지 않는 문자열만 결과 배열에 추가합니다.
            result.append(string)
    return result