class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ret = 0
        
        for i in range(32):
            if (x & (1<<i) != y & (1<<i)):
                ret += 1
        
        return ret