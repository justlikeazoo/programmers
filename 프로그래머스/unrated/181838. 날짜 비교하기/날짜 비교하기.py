def solution(date1, date2):
    # date1의 연도, 월, 일을 각각 변수에 저장합니다.
    year1, month1, day1 = date1
    
    # date2의 연도, 월, 일을 각각 변수에 저장합니다.
    year2, month2, day2 = date2
    
    # date1이 date2보다 앞서는지 비교합니다.
    if year1 < year2:
        return 1
    elif year1 > year2:
        return 0
    else:
        if month1 < month2:
            return 1
        elif month1 > month2:
            return 0
        else:
            if day1 < day2:
                return 1
            elif day1 > day2:
                return 0
            else:
                return 0  # date1과 date2가 동일한 경우
