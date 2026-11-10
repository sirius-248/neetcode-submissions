class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[k-1]:
                k+=1
                nums[k-1]=nums[i]
                
        return k