class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum1 = 0
        sum2 = 0
        length = len(a)
        len2 = len(b)
        for i in range(0, length):
            sum1+= int(a[length-i-1])*pow(2, i)
        for i in range(0, len2):
            sum2+= int(b[len2-i-1])*pow(2, i)
        n = sum1 + sum2
        print(sum2)
        print(sum1)
        binaryNum = ''
        while (n > 0):  
            binaryNum+=str( n % 2 )
            n = int(n / 2)
        if(binaryNum == ''):
            return "0"
        return (binaryNum[::-1])