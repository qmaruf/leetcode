class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ret = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            j = i + 1
            k = len(nums) - 1            
            
            while (j < k):
                currsum = nums[j] + nums[k]
                target = -nums[i]
                
                if j - 1 > i and nums[j] == nums[j-1]:
                    j += 1
                    continue
                
                if k + 1 < len(nums) and nums[k] == nums[k+1]:
                    k -= 1
                    continue
                
                if currsum < target:
                    j += 1
                elif currsum > target:
                    k -= 1
                else:                    
                    ret.append((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                    
        return ret
                    
                    
        
