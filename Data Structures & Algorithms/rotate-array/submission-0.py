
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
       k=k%len(nums)
       left=[]
       if k==0:
        return
       for i in nums[k:]:
        left.append(i)
       for i in nums[0:k]:
        left.append(i)
       for i in range(len(nums)):
        nums[i]=left[i]
        