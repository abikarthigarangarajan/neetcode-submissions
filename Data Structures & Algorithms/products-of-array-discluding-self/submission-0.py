class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        post=nums[0]
        n=len(nums)
        res=[0] * n
        for i in range(n):
            if i==0:
                res[0]=1
            else:
                res[i] = post
                post*=nums[i]
        pre=nums[n-1]
        for i in range(n-1,-1,-1):
            if i==n-1:
                res[n-1]*=1
            else:
                res[i]*=pre
                pre*=nums[i]
        return res


        