class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if(k == len(num)):
            return "0"
        s=[]
        n=len(num)
        for i in range(n):
            while len(s)>0 and k > 0 and s[-1]>(num[i]):
                s.pop()
                k-=1
            s.append((num[i]))
        while k:
            s.pop()
            k-=1
        while len(s) > 0 and s[0] == '0':
            s.pop(0)
        if len(s) == 0:
            return '0'
        return ''.join(s)