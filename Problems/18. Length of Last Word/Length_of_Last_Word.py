class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
                s = s.split(' ')
                        i = len(s) - 1
                 while i>=0:
            if str(s[i]) == '':
                pass
            else:
                return len(s[i])
            i-=1
                    return 0