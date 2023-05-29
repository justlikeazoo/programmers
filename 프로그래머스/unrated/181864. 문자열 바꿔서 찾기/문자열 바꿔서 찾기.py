def solution(myString, pat):
    # myString에서 "A"를 "B"로, "B"를 "A"로 바꾼 문자열을 생성합니다.
    transformed_string = myString.replace("A", "x").replace("B", "A").replace("x", "B")

    # pat이 변환된 문자열에 포함되어 있는지 확인합니다.
    if pat in transformed_string:
        return 1
    else:
        return 0