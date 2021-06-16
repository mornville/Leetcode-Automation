class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
                for char in S:
            if str(char).isalpha():
                stack.append(char)
                        ans = ''
                for char in S:
            if char.isalpha():
                ans+=stack.pop()
            else:
                ans+=char
                        return ans
                                                