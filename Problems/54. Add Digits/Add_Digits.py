class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum = 0
        while(num > 0 or sum > 9): 
            if(num == 0): 
                num = sum
                sum = 0
            sum += num % 10
            num /= 10
        return int(sum)
                