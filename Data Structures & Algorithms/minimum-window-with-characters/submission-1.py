class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        resl = float('infinity')
        res = ""
        hmt={}
        for c in t:
            hmt[c]=hmt.get(c,0)+1
        need = len(hmt)
        have = 0
        hmw={}
        l=0
        
        for r in range(len(s)):
            if s[r] in hmt:
                hmw[s[r]] = hmw.get(s[r],0)+1
                if hmw[s[r]]==hmt[s[r]]:
                    have+=1          
            while (have==need) :
                tresl = r-l+1
                if tresl<resl:
                    resl=tresl
                    res=s[l:r+1]
                if s[l] in hmt:
                    hmw[s[l]]-=1
                    if hmw[s[l]]<hmt[s[l]]:
                        have-=1
                l+=1
        return res


        
        