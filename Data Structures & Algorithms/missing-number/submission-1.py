class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        expected=0
        for i in range(0,n+1):
            expected+=i
        actual=sum(nums)
        return expected-actual