class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:  
        #find half size
        m=len(nums1)
        n=len(nums2)
        total=m+n
        half=total//2

        if n<m:
            nums1,nums2=nums2,nums1

        #start with any array to find partitions
        #you are not required to sort induvidual parts, you are just need to 
        #find the half
        l=-1
        r=len(nums1)-1
        while(l<=r):
            i=(l+r)//2 #a index
            j=half-i-2 #b index

            Aleft = nums1[i] if i>=0 else float("-infinity")
            Aright = nums1[i+1] if (i+1) < len(nums1) else float("infinity")
            Bleft = nums2[j] if j>=0 else float("-infinity")
            Bright = nums2[j+1] if (j+1)<len(nums2) else float("infinity")

            if Aleft<=Bright and Bleft<=Aright:
                if (total%2):
                    return min(Aright,Bright)
                else:
                        m1=max(Aleft,Bleft)
                        m2=min(Aright,Bright)
                        return (m1+m2)/2
            elif Aleft>Bright:
                r=i-1
            else:
                l=i+1

       
        



        
            



        