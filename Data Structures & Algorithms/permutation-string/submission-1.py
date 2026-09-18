class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        hs1=[0]*26 
        hs2=[0]*26
        match=0
        for i in s1:
            c=ord(i)-ord('a')
            hs1[c]=hs1[c]+1
        for i in range(len(s1)):
            d=s2[i]
            c=ord(d)-ord('a')
            hs2[c]+=1
        for i in range(26):
            if hs1[i]==hs2[i]:
                match+=1
        l=0
        for r in range(len(s1),len(s2)):
            if (match==26):
                return True
            
            # LEFT CHARACTER
            #CHECK LEFT CHARACTER AND REMOVE
            idx = ord(s2[l])-ord('a')

            if hs2[idx]==hs1[idx]:
                match-=1

            hs2[idx]-=1

            if hs2[idx]==hs1[idx]:
                match+=1

            
            
            #RIGHT CHARACTER
            idx = ord(s2[r])-ord('a')
            if hs2[idx]==hs1[idx]:
                match-=1
            hs2[idx]+=1

            if hs2[idx]==hs1[idx]:
                match+=1
        
            l+=1
        return match==26
            



            
        

        