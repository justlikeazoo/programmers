from collections import defaultdict

def solution(strArr):
    group_counts = defaultdict(int)

    for string in strArr:
        length = len(string)
        group_counts[length] += 1

    max_count = max(group_counts.values())

    return max_count