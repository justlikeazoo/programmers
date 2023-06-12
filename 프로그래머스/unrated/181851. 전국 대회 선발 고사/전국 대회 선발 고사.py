def solution(rank, attendance):
    answer=0
    cnt=0
    
    for i in range(1,len(rank)+1):
        num=rank.index(i)
        
        if attendance[num]:
            answer += num * 100 ** (2 - cnt)
            cnt += 1
        
        if cnt == 3:
            break
    return answer