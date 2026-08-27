class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        while l<r:
            nt=numbers[l]+numbers[r]
            if nt<target:
                l+=1
            elif nt>target:
                r-=1
            else:
                return [l+1,r+1]
        return []

        