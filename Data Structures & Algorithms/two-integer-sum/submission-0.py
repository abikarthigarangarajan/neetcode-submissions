class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        n=len(nums)
        for i in range (n):
            tf = target-nums[i]
            if tf in hm:
                return [hm[tf],i]
            hm[nums[i]]=i
        return []