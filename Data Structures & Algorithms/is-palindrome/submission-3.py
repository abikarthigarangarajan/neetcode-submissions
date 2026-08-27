class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r:
            while (not self.alphanum(s[l])) and l<r:
                l+=1
            while (not self.alphanum(s[r])) and l<r :
                    r-=1
            lc=s[l].lower()
            rc=s[r].lower()
            if lc!=rc:
                return False
            l+=1
            r-=1
        return True
    
    def alphanum(self,c):
        return (ord('A')<=ord(c)<=ord('Z') or ord('a')<=ord(c)<=ord('z') or ord('0')<=ord(c)<=ord('9'))
         
        