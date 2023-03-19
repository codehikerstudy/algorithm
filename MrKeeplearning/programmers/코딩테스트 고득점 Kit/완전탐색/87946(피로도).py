from itertools import permutations

"""
초기에는 단순히 소모 피로도가 낮은 순으로 정렬을 한 상태에서
진행하면 쉽게 구할 수 있지 않을까라는 생각으로 sort()를 사용했지만,
소모 피로도가 낮은 순으로 정렬하더라도 만약 다음 순으로 나오는 최소 필요 피로도가 너무 높다면
최대한 많은 탐색 횟수를 올바르게 검색할 수 없다.
"""
def solution1(k, dungeons):
    count = 0
    dungeons.sort(key=lambda x: x[1])
    for i in dungeons:
        if k >= i[0]:
            k -= i[1]
            count += 1
    return count


"""
최대한 많은 탐험 횟수를 구하기 위해 필요한 조건에 따라 dungeons 리스트를 재배열하는 것은 그 조건을 생각하기 까다롭다.
따라서, 단순히 가능한 모든 순서를 permutations()로 찾아내고, 그것들을 돌아보는 것도 한 가지 방법이 될 수 있다.
"""
def solution2(k, dungeons):
    count_list = []

    # 순열을 사용해서 가능한 모든 케이스를 살펴본다.
    for case in permutations(dungeons, len(dungeons)):
        # 각 케이스마다 피로도와 탐험한 던전 수는 매번 초기화되어야 한다.
        fatigue = k
        count = 0
        for i in case:
            # 던전의 최소 필요 피로도보다 현재의 피로도가 더 높아야 탐험이 가능하다.
            if fatigue >= i[0]:
                fatigue -= i[1]
                count += 1

        # 순열의 모든 케이스 별로 나온 탐험 횟수를 count_list에 담고
        # max함수를 통해서 가장 큰 값을 추출하여 return한다.
        count_list.append(count)

    return max(count_list)


print(solution2(80, [[80, 20], [50, 40], [30, 10]]))
