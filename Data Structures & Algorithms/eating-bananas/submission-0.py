class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k value lies btw 1 and max[piles](default ans)
        l=1
        r=max(piles,default=0)
        kt=r

        while(l<=r):
            m=(l+r)//2
            ans = 0
            for i in piles:
                ans+=(math.ceil(i/m))
            if ans>h:
                l=m+1
            else:
                kt = min(kt,m)
                r=m-1
                
        return kt

