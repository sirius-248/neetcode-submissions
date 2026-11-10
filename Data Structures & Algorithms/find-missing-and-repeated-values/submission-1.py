class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen=set()
        for i in grid:
            for j in i:
                if j in seen:
                    rep=j
                else:
                    seen.add(j)
        n=len(grid[1])
        sum=0
        for i in range(1,n**2+1):
            sum+=i
        sumr=0
        for i in grid:
            for j in i :
                sumr+=j
        sumr-=rep
        miss=sum-sumr
        return [rep,miss]