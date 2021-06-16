class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for char in s: 
            # upper char
            if stack and stack[-1].isupper() and stack[-1].lower() == char:
                stack.pop()
            # lower char
            elif stack and stack[-1].islower() and stack[-1].upper() == char:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)