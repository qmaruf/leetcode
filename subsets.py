class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:        
        ret = []
        
        def solve(curr, pos):
            if pos >= len(nums):
                return            
            ret.append(curr)
            for i in range(pos+1, len(nums)):
                solve(curr + [nums[i]], i)
        
        solve([], -1)
        return ret
                
        
        
