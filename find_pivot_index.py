class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i-1]
        
        for i in range(n):
            rightval = nums[n-1] - nums[i]
            leftval = 0 if i == 0 else nums[i-1]            
            if leftval == rightval:
                return i
        return -1
        
