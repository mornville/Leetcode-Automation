class Solution(object):
    def wordPattern(self, pattern, str):
        words = str.split(' ')
        if len(set(list(pattern))) != len(set(words)):
            return False
                        wordDict = {}
        index = 0
        length = len(pattern)
        for i in words:
            if index >= length:
                return False
            key = pattern[index]
            if key in wordDict and wordDict[key] != i:
                return False
            elif key not in wordDict:
                wordDict[key] = i
            index += 1
        return True
                    