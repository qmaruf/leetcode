class Solution:
    
    def search(self, c1, pos, t):
        for i in range(pos, len(t)):
            if t[i] == c1:
                return i
        return -1
    
    def isSubsequence(self, s: str, t: str) -> bool:        
        pos = -1
        for c1 in s:
            pos = self.search(c1, pos+1, t)            
            if pos == -1:
                return False
        return True
            
        
