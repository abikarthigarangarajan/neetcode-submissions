class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hsr=set()
        hsc=set()
        hm=defaultdict(set)
        for i in range(9):
            hsr=set()
            for j in range(9):
                e=board[i][j]
                if e==".":
                    continue
                if e in hsr:
                    return False
                hsr.add(e)
                
        for j in range(9):
            hsc=set()
            for i in range(9):
                e=board[i][j]
                if e==".":
                    continue
                if e in hsc:
                    return False
                hsc.add(e)

        for i in range(9):
            for j in range(9):
                    e=board[i][j]
                    if e==".":
                        continue
                    r=(i//3)
                    c=(j//3)
                    if e in hm[(r,c)]:
                        return False
                    hm[(r,c)].add(e)
            
        return True
            


                



        