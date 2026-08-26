class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs=set()
        res=0
        for i in nums:
            hs.add(i)
        for i in nums:
            if (i-1) in hs:
                continue
            tr=0
            n=i
            while (n) in hs:
                tr+=1
                n=n+1
            res=max(tr,res)
        return res


        