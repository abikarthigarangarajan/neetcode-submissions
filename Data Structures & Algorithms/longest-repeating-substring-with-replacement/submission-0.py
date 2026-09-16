class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        lg=0
        res=0
        mf=0
        hm={}
        l=0

        for r in range(n):
            c=s[r]
            hm[c]=hm.get(c,0)+1
            if hm[c]>mf:
                mf=hm[c]
            if (r-l+1)-mf>k:
                c=s[l]
                hm[c]=hm[c]-1
                lg-=1
                l+=1
            res = max(r-l+1,res)
        return res
            


        