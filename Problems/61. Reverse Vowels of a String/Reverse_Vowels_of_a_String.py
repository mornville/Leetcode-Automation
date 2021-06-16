class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = list(s)
        vowels = 'aeiouAEIOU'
        start = 0
        end = len(s) - 1
        while start < end:
            if ans[start] in vowels and ans[end] in vowels:
                ans[start], ans[end] = ans[end], ans[start]
                start += 1
                end -= 1
            if ans[start] not in vowels:
                start += 1
            if ans[end] not in vowels:
                end -= 1
        return "".join(ans)
        