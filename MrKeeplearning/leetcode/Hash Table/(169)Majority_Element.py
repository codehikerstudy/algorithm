import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
            Counter객체의 사용법과 파이썬의 딕셔너리는 items() 메소드를 사용했을 때
            key와 value를 for문으로 조회하는 것이 가능하다는 점을 인지하고 있다면 쉽게 풀 수 있다.
        """
        count = collections.Counter(nums)
        for k,v in count.items():
            if v > len(nums)//2:
                return k

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
            Since the count of majority element will be atleast n//2 + 1 therefore,
            if we make a number as majorityElement and keep on incrementing the count if we encounter that element again and decrement the count if any other element is encountered then the majority element will have atleast 1 in count. Whenever the count becomes 0, reinitialise the majority element with current number.
            For example, nums = [2,2,1,1,1,2,2]
            Let's say majorityElement is 2 therefore count will be 1.
            Nove move ahead and again 2 is encountered so count will be incremented and become 2.
            Now 1 is encountered so count will be decremented and become 1
            Now again 1 is encountered so count will be decremented and become 0
            Now 1 is encountered but count is 0 so initialize 1 as majority element and count to 1 again.
            Now 2 is encountered so count will be decremented and become 0
            Now again 2 is encountered but count is 0 so initialize 2 as majority element and count to 1 again.
            Now no more elements are left so just return the majprity element.
        """
        count = 0
        majorElement = None
        for num in nums:
            if count == 0:
                majorElement = num
            count += 1 if majorElement == num else -1
        return majorElement