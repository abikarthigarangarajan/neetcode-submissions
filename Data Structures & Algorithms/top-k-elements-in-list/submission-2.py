class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm={}
        res=[]
        for n in nums:
            hm[n]=hm.get(n,0)+1
        arr=[]
        for n in hm:
            arr.append([hm[n],n])
        arr.sort()
        n=len(arr)
        res=[]
        for i in range(n-1,-1,-1):
            m=len(res)
            if m<k:
                res.append(arr[i][1])
                m+=1
        return res

         
        