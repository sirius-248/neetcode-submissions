class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s2=""
        max_l=0
        for ch in s:
            while ch in s2:
                s2=s2[1:]
            s2+=ch
            max_l=max(max_l,len(s2))
        return max_l
