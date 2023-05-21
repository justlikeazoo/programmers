def solution(num_list):
    odd_sum = sum(num_list[0::2])  # 홀수 번째 원소들의 합
    even_sum = sum(num_list[1::2])  # 짝수 번째 원소들의 합
    
    return max(odd_sum, even_sum)