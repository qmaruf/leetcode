class Solution:
    def letterCombinations(self, digits: str) -> List[str]:        
        def solve(digits):
            if len(digits) == 0:
                return []
            ret = []
            q = []
            q.append("")         
            while len(q):
                curr = q.pop(0)
                depth = len(curr)
                if depth == len(digits):
                    ret.append(curr)
                else:
                    word = keys[digits[depth]]                       
                    for ch in word:
                        q.append(curr+ch)            
            return ret
        keys = {
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",            
            '8':"tuv",
            '9':"wxyz"
        }
        
        ret = solve(digits)
        return ret
        
