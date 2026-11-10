class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        subset=[]
        def backtrack(i,total):
            if total>target or i==len(nums):
                return
            if total==target:
                result.append(subset.copy())
                return
            subset.append(nums[i])
            backtrack(i,total+nums[i])
            subset.pop()
            backtrack(i+1,total)
        backtrack(0,0)
        return result

        