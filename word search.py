class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visit = set()
        
        def solve(i, j, sz):            
            if sz == len(word):
                return True
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return False
            if board[i][j] != word[sz] or (i, j) in visit:
                return False
            
            
            visit.add((i, j))
            
            ret = solve(i+1, j, sz+1) or \
                  solve(i-1, j, sz+1) or \
                  solve(i, j-1, sz+1) or \
                  solve(i, j+1, sz+1)
            
            visit.remove((i, j))
            
            return ret
            
            
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    visit = set()
                    if solve(i, j, 0):
                        return True
        return False
                        
        
