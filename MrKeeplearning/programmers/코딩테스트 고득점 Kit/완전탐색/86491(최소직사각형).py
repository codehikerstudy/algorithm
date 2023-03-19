class Solution1:
    """
    sizes에 담긴 모든 원소를 하나의 리스트 arr에 담는다.
    arr를 오름차순으로 정렬한다.

    정렬된 arr에서 중간값을 구한다. arr은 항상 짝수일 수 밖에 없기 때문에
    중간값은 arr의 길이를 2로 나누었을 때의 몫으로 한다.

    중간값 바로 앞의 수와 arr의 마지막 수를 곱하면 답을 구할 수 있지 않을까? 라는 생각에 시도해봤지만
    테스트케이스에서는 통과해도 제출 시 몇 몇 케이스를 통과하지 못해 실패했습니다.
    """

    def solution(self, sizes):
        arr = []
        for i in sizes:
            arr.append(i[0])
            arr.append(i[1])
        arr.sort()
        # 가로 x 세로 이기 때문에 항상 arr의 길이는 짝수일 수 밖에 없다.
        # 따라서 중간값의 인덱스(medium_idx)를 2로 나누었을 때 몫으로 한다.
        medium_idx = len(arr) // 2
        answer = arr[medium_idx - 1] * arr[-1]
        return answer


class Solution2:
    """
    핵심 아이디어: 우선 한쪽 길이에서 만큼은 모든 길이를 포용할 수 있는 길이를 지정한다. -> 가장 긴 길이를 찾아 설정.

    명함의 길이가 "가로x세로"의 형식으로 주었지만,
    명함을 두는 방식은 정해져 있지 않기 때문에 반드시 주어진 순서를 유지할 필요가 없다.

    따라서, 하나의 리스트에 모든 값들을 담기보다는 왼쪽에는 큰 값을,
    오른쪽에는 작은 값을 두는 방향으로 주어진 sizes 리스트의 순서를 수정한다.

    [[큰 값, 작은 값], ...]

    한 쪽의 길이는 가장 큰 값으로 설정을 한 상태이기 때문에 나머지 작은 값을 정한다.

    작은 값들 중에서도 가장 큰 값을 선택해 해당 길이를 지정한다.
    """
    def solution(self, sizes):
        # sizes의 요소는 리스트 형태이고 이 리스트 내부의 값을 내림차순 형태로 정렬한다.
        sizes = [sorted(size, reverse=True) for size in sizes]
        widths = [size[0] for size in sizes]
        heights = [size[1] for size in sizes]
        width, height = max(widths), max(heights)
        answer = width * height
        return answer


sizes1 = [[60, 50], [30, 70], [60, 30], [80, 40]]
sizes2 = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
sizes3 = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

sol1 = Solution1()
print(sol1.solution(sizes1))

sol2 = Solution2()
print(sol2.solution(sizes1))