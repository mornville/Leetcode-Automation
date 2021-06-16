class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        stack.append(-1)
        count = 0
        for char in s:
            if (stack[-1] == 'R' and char == 'L') or (stack[-1] == 'L' and char == 'R'):
                stack.pop()
            else:
                stack.append(char)
                        if stack[-1] == -1:
                count+=1
                        return count