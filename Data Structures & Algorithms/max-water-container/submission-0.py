class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        res=0
        while (l<r):
            mi=min(heights[l],heights[r])
            tr=(r-l)*mi
            res=max(res,tr)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return res
            


        