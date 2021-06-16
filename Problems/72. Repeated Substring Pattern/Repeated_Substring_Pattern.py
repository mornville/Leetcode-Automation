class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n < 1:
            return False
        temp = ''
        idx = 0
        while idx <= (n//2) and idx != (n-1):
            temp+=s[idx]
            if n % (idx+1) == 0:
                if temp * (n/(idx+1)) == s:
                    return True
            idx+=1
                    return False