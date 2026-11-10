class Solution:
    def groupAnagrams(self,strs:List[str])-> List[List[str]]:
        groups={}
        for word in strs:
            newword="".join(sorted(word))
            if newword in groups:
                groups[newword].append(word)
            else:
                groups[newword]=[word]
        fr=[]
        for word in groups:
            fr.append(groups[word])
        return fr
        