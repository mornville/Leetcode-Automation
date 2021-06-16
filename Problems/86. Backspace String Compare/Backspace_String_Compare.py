class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def convertToString(string):            
            stack = []
            for char in string:
                if char!='#':
                    stack.append(char)
                else:
                    if stack:
                        stack.pop()
                    else:
                        pass
            return "".join(stack)
                       return convertToString(S) == convertToString(T)