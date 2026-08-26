class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
                return False
        arr=[0]*26
        for i in s:
            ind=ord(i)-ord('a')
            arr[ind]+=1
        for i in t:
            ind=ord(i)-ord('a')
            arr[ind]-=1
            if arr[ind]<0:
                return False
        return True
            

        