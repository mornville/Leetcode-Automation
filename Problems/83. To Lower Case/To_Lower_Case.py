class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ''
        for char in s:
            ans+=char.lower()
        return ans