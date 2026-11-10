class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        max_count=0
        max_element=float('-inf')
        for i in count:
            if count[i]>max_count:
                max_count=count[i]
                max_element=i
        return max_element