class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minip=prices[0]
        maxp=0
        for i in prices:
            if i<minip:
                minip=i
            maxp=max(maxp,i-minip)
        return maxp