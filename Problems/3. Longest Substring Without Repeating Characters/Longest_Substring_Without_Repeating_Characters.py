class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maximum = 0
        substring = ""
        for idx, c in enumerate(s):
            if c in substring:
                substring = substring[substring.find(c)+1:]
            substring += c
            if len(substring) > maximum:
                maximum = len(substring)
        return maximum