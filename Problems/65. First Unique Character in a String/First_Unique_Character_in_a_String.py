class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)
                for idx, char in enumerate(s):
            if count[char] == 1:
                return idx
        return -1