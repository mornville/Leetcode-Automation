class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        ans = []
        lastIndex = {}
        for idx, char in enumerate(S):
            lastIndex[char] = idx
        start = end = 0
                for idx, char in enumerate(S):
            end = max(end, lastIndex[char])
            if idx == end:
                ans.append(idx - start + 1)
                start = idx + 1
                        return ans                