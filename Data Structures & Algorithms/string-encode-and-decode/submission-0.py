class Solution:

    def encode(self, strs: List[str]) -> str:
        es=""
        for s in strs:
            n=len(s)
            es += str(n)+'#'+s
        return es


    def decode(self, s: str) -> List[str]:
        i=0
        res=[]
        n=len(s)
        while i<n:
            m=""
            while s[i]!='#':
                m=m+s[i]
                i+=1
            m=int(m)
            ts=s[i+1:i+m+1]
            res.append(ts)
            i=i+m+1
        return res

