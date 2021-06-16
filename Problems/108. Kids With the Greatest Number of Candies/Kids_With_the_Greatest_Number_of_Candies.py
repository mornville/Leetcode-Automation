class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maximum = max(candies)
        i = 0
                while i < len(candies):
            if (candies[i]+extraCandies) >= maximum:
                candies[i]  = True
            else:
                candies[i] = False
            i+=1
                    return candies