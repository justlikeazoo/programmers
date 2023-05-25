def solution(myString):
    words = myString.split("x")  # "x"를 기준으로 문자열을 분할하여 리스트로 저장합니다.
    lengths = [len(word) for word in words]  # 분할된 각 문자열의 길이를 순서대로 저장합니다.
    return lengths