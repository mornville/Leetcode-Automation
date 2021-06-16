class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low, high = 0, num
        if num == 1:
            return True
        while low<=high:
            mid = (low+high)//2
            if mid*mid == num:
                return mid
            elif mid*mid>num:
                high = mid-1
            else:
                low = mid+1
        return False
            