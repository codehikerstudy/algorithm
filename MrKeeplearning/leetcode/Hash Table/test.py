s = "bbbbb"

substring = set()
result = 0
j = 0

for i in range(len(s)):
    # 만약 substring 안에 이미 해당 요소가 있다면 해당 요소는 삭제
    while s[i] in substring:
        substring.remove(s[j])
        j += 1
    # substring 안에 없으면 추가
    substring.add(s[i])
    # 가장 긴 substring의 문자열 자체를 반환하는 것이 아닌
    # 단순히 해당 substring의 길이만 반환하는 것이기 때문에
    # 굳이 문자열을 저장하는 공간을 마련할 필요가 없이 매순간 길이만 확인하면 된다.
    # max(result, len(substring))에서 len(substring)은 현재 위치에서 substring의 길이를 말한다.
    # 그리고 result에는 for문 전체를 도는 동안 가장 긴 substring의 길이만 기록된다.
    result = max(result, len(substring))

print(result)