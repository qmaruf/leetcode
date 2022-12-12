class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:        
        ret = []
        
        def solve(curr, used):
            if len(curr) == len(nums):
                ret.append(curr)
            for i, n in enumerate(nums):
                if used[i] == 0:
                    used[i] = 1
                    solve(curr + [n], used)
                    used[i] = 0
            
        
        solve([], [0]*len(nums))
        return ret
        
