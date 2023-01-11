from collections import Counter

'''
1. 해당 문제는 완주한 사람 이름(key)와 완주 여부(0 혹은 1)로 나누어 hash 형태로 문제를 풀이함
2. 동명이인의 경우도 고려하여 동명이인일 경우 value가 음수로 나올 수 있도록 고려
3. 코드가 간결하지 못하다는 점이 아쉬움
'''
def solution(participant, completion):
    dic_part = Counter(participant)
    for i in completion:
        if i in dic_part.keys():
            dic_part[i] -= 1
            
    for j in dic_part:
        # value의 값이 변하지 않았거나(dic_part[j] == 1), 동명이인의 경우로 value값이 음수가 나온 경우(dic_part[j] < 0)
        if dic_part[j] == 1 or dic_part[j] < 0:
            return j
    