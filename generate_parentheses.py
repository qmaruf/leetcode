class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def solve(curr, op, cl, to):
            if (op == to and cl == to):
                ret.append(curr)
            if cl < op:
                solve(curr + ")", op, cl + 1, to)
            if op < to:
                solve(curr + "(", op + 1, cl, to)
                
            
        
        ret = []
        solve("", 0, 0, n)
        print (ret)
        return ret
        
