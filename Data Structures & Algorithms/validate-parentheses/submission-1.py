"""class Solution:     Stack APPROACH 
    def isValid(self, s: str) -> bool:
        pairs={')':'(',"]":"[","}":"{"}
        stack=[]
        for ch in s:
            if ch in "{([":
                stack.append(ch)
            else:
                if not stack:
                    return False
                else:
                    if pairs[ch] ==stack[-1]:
                        stack.pop()
                return True"""
class Solution :
    def isValid(self,s:str)->bool:
        while "()" in s or "{}" in s or "[]" in s:
            s=s.replace("()","")
            s=s.replace("[]","")
            s=s.replace("{}","")
        return s==""