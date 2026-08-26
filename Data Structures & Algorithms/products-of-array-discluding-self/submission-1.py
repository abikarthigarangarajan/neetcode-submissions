class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        post=1
        n=len(nums)
        res=[1] * n
        for i in range(n):
            res[i] = post
            post*=nums[i]
        pre=1
        for i in range(n-1,-1,-1):
            res[i]*=pre
            pre*=nums[i]
        return res


        