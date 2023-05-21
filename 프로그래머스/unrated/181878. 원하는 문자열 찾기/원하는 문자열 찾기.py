def solution(myString, pat):
    myString = myString.lower()
    pat = pat.lower()
    return int(pat in myString)