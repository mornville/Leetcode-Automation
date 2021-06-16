class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        count = 0
        p1 = 0
        ans = ''
        while p1<len(S):
            if S[p1] == '(':
                count+=1
                if count>1:
                    ans+=S[p1]
            else:
                count-=1
                if count>0:
                    ans+=S[p1]
            p1+=1
        return ans