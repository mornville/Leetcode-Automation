class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dictionary = collections.Counter(s)
        temp = [(char,freq) for char,freq in sorted(dictionary.items(), key=lambda x: (-x[1], x))]
        res = [i*j for i, j in temp]
        return ''.join(res)