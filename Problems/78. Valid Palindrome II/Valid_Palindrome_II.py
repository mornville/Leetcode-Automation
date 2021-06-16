class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                # delete left
                one = s[left+1:right+1]
                # delete right
                two = s[left:right]
                return one == one[::-1] or two == two[::-1]
            left += 1
            right -= 1
        return True