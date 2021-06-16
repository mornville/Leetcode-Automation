class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(" ")
        ans = {}
        for word in s:
            (ans[word[-1]]) = word[:-1]
        quit = ''
        for i in range(1, len(s)):
            if str(i) in ans.keys():
                quit  = quit + ans[str(i)] + ' '
        return quit + ans[str(len(s))]
                                