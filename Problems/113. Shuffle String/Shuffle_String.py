class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        temp = [None]*len(s)
                for idx, char in enumerate(s):
            temp[indices[idx]] = char
                    return "".join(temp)