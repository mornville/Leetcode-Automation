class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
                for element in ops:
            if element == 'C':
                if stack:
                    stack.pop()
                else:
                    pass
            elif element == 'D':
                if stack[-1]:
                    stack.append(int(stack[-1] * 2))
                else:
                    pass
            elif element == '+':
                if stack[-1] and stack[-2]:
                    stack.append(int(stack[-1]) + int(stack[-2]))
                elif stack[-1]:
                    stack.append(int(stack[-1]))
            else:
                stack.append(int(element))
                    return sum(stack)