class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #find row and columns
        r=len(matrix)
        c=len(matrix[0])

        #bs on rows to find the specific row the element ies on
        top=0
        bot=r-1
        while(top<=bot):
            tr=(top+bot)//2
            if target>matrix[tr][-1]:
                top=tr+1
            elif target<matrix[tr][0]:
                bot=tr-1
            else:
                break
        if not(top<=bot):
            return False
        tr=(top+bot)//2
        
        #bs on tr row 
        l=0
        r=c-1
        while(l<=r):
            m=(l+r)//2
            if target<matrix[tr][m]:
                r=m-1
            elif target>matrix[tr][m]:
                l=m+1
            else:
                return True
        return False


        