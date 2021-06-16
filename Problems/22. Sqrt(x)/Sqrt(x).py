class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low, high = 0, x + 1
        while low < high:
            mid = (low + high) // 2
            if mid * mid > x:
                high = mid
            else:
                low = mid + 1
        return low - 1