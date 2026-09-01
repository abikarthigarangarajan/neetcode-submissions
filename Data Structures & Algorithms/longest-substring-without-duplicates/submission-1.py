class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        hm={}
        l=0
        r=0
        ll=0
        for r in range(n):
            if s[r] in hm:
                l = max(hm[s[r]]+1 , l)
            hm[s[r]]=r
            ll=max(ll,r-l+1)
        return ll

        