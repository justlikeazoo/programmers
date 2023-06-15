def solution(str_list, ex):
    tail_string=""
    for string in str_list:
        if ex not in string:
            tail_string+=string
    return tail_string