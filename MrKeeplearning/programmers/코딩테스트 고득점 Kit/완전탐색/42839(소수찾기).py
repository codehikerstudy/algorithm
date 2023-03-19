# 1. prime_set을 정의한다.
prime_set = set()

def isPrime(number):
    # 6. 0과 1은 제외
    if number in (0, 1):
        return False

    # 7. 에라토스테네스의 체 개념을 적용하여 소수인지 확인
    lim = int(number ** 0.5 + 1)
    for i in range(2, lim):
        if number % i == 0:
            return False
    return True

def recursive(combination, others):
    """
    :param combination: 지금까지 조합된 숫자
    :param others: 아직 사용하지 않은 숫자
    """
    # 5. 탈출 조건 / 비교조건: 지금까지 만들어진 조합을 소수인지 판단
    if combination != "":
        if isPrime(int(combination)):
            prime_set.add(int(combination))
    # 4. 현재까지 만들어진 숫자에 남아있는 숫자 중 하나를 더 추가해 조합을 생성
    for i in range(len(others)):
        recursive(combination + others[i], others[:i] + others[i + 1:])



def solution(numbers):
    # 2. 모든 조합을 만드는 재귀함수를 수행한다.
    # "recursive 함수에서 여태까지 만들어진 숫자는 없는데, 앞으로 써야 하는 숫자는 numbers 전체이다."를 의미
    recursive("", numbers)

    # 3. prime_set의 길이를 반환한다.
    return len(prime_set)
