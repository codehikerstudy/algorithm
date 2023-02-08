class MedianFinder:

    def __init__(self):
        self.arr = []
        self.count = 1

    def addNum(self, num: int) -> None:
        self.arr.append(num)

        # arr에 새로운 num을 추가할 때마다 count에 -1을 곱함
        # count = -1일 때 arr 길이는 홀수
        # count = 1일 때 arr 길이는 짝수
        self.count *= -1

    def findMedian(self) -> float:
        self.arr.sort()
        median_idx = len(self.arr)//2

        if self.count == -1:
            median = self.arr[median_idx]
        else:
            median = (self.arr[median_idx] + self.arr[median_idx - 1])/2

        return median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()