class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s={}
        count_t={}
        if len(s)!=len(t):
            return False
        for i in s:
            count_s[i]=count_s.get(i,0)+1
        for i in t:
            count_t[i]=count_t.get(i,0)+1
        for i in s:
            if i not in count_t or count_s[i]!=count_t[i]:
                return False
        return True
        