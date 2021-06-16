class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n < 0:
            x = 1/x
            n = -n
                curProduct = x
        res = 1
        while n > 0:
            if n % 2 == 1:
                res *= curProduct
                        curProduct *= curProduct
            n //= 2
                return res