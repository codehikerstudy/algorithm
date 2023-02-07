'''
- 리트코드 295번 문제: find-median-from-data-stream
- 문제 출처: https://leetcode.com/problems/find-median-from-data-stream/
- 해당 문제 풀이는 직접 푼 풀이입니다.
'''

'''
- 해당 문제는 median을 구하기 위해 sort()를 활용하였습니다.
- 처음에는 addNum 함수에 self.sol.sort()를 작성하였는데, 이러한 결과 마지막 테스트 케이스에서 "time limit exceeded"가 발생하였습니다.
    정확한 원인은 모르겠으나 개인적으로 숫자를 추가할 때마다 정렬하는 것보단 median을 찾을 때마다 정렬하는 것이 더 빠를 것 같다고 판단하여
    findMedian 함수에 self.sol.sort()를 작성하였고, 이러한 결과 모든 테스트 케이스가 통과하여 성공적으로 제출되었습니다.
    findMedian 함수에 self.sol.sort()를 작성하여 성공한 결과는 아래와 같습니다.
    - Runtime: 3136 ms, faster than 8.13% of Python3 online submissions for Find Median from Data Stream.
    - Memory Usage: 35.9 MB, less than 72.37% of Python3 online submissions for Find Median from Data Stream.

- 문제 풀이 방법:
1. addNum()
    - 해당 함수는 단순히 숫자를 추가시키는 함수이므로 sol 배열에 매개변수 num을 추가하는 코드를 작성한다.
        self.sol.append(num)
2. findMedian()
    - 해당 함수는 배열의 길이가 홀수일 경우 배열의 가장 가운데 숫자를, 짝수일 경우 중앙의 두 값 사이의 평균을 반환하도록 작성함.
    - 우선 Median을 구하기 위해 배열을 정렬한다. (문제에서도 'The median is the middle value in an ordered integer list.' 라고 언급하였다)
        self.sol.sort()
    - 배열의 길이가 짝수일 경우 두 중간 값의 평균을 반환
        if (len(self.sol) % 2) == 0:
            return (self.sol[(len(self.sol) // 2) - 1] + self.sol[len(self.sol) // 2]) / 2
    - 배열의 길이가 홀수일 경우 배열의 중간 값을 반환
        else:
            return self.sol[len(self.sol) // 2]
'''
class MedianFinder:

    def __init__(self):
        self.sol = []
        
    def addNum(self, num: int) -> None:
        self.sol.append(num)

    def findMedian(self) -> float:
        # median 혹은 두 중간 값의 평균을 반환하기 위해 sol 배열을 정렬한다.
        self.sol.sort()
        
        # 만약 배열 sol의 길이가 짝수일 경우 두 중간 값의 평균을 반환
        if (len(self.sol) % 2) == 0:
            return (self.sol[(len(self.sol) // 2) - 1] + self.sol[len(self.sol) // 2]) / 2

        # 만약 배열 sol의 길이가 홀수일 경우 중간 값을 반환
        else:
            return self.sol[len(self.sol) // 2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()