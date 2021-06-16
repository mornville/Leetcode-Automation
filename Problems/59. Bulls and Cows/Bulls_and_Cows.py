class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
                bulls = 0
                for idx, char in enumerate(secret):
            if char == guess[idx]:
                bulls+=1
                        cows = 0
                cows = sum((Counter(secret)&Counter(guess)).values()) - bulls
                return str(bulls) + "A" + str(cows) + "B"