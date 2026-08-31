class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        maxp=[0]*n
        mp=0
        ms=0
        maxs=[0]*n
        sum=0
        for i in range(n):
            maxp[i]=mp
            mp=max(height[i],mp)
        for i in range(n-1,-1,-1):
            maxs[i]=ms
            ms=max(height[i],ms)
        for i in range(n):
            mini=min(maxs[i],maxp[i])
            t = (mini-height[i])
            if t>0:
                sum += t
        return sum

        




        