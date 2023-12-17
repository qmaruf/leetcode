class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm = dict()
        for i, n1 in enumerate(nums):
            n2 = target - n1
            if n2 in hm:
                j = hm[n2]
                return [j, i]
            hm[n1] = i   
