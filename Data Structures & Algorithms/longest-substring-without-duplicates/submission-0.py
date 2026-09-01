class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ll=0
        l=0
        r=0
        hs=set()
        n=len(s)
        while r<n:
            while s[r] in hs and l<=r:
                hs.remove(s[l])
                l+=1
            hs.add(s[r])
            lt=(r-l+1)
            ll=max(lt,ll)
            r+=1
        return ll
