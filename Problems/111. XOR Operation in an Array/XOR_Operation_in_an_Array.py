class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        xor = start
        i = 1
                while i<n:
            temp = start + 2*i
            xor = xor ^ temp
            i+=1
                    return xor
                