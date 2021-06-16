class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
#         stack = []
#         temp = ""
#         i = 0 
#         while i < len(s):
#             if s[i]!=' ':
#                 temp+=s[i]
#             elif s[i] == ' ' and temp!= "":
#                 stack.append(temp)  
#                 temp = ""
                #             if i == len(s) - 1 and s[i]!=" ":
#                 stack.append(temp)
                #             i+=1
        #         return ' '.join(stack[::-1])
        return ' '.join(s.split()[::-1])