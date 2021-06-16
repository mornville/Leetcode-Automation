class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        time = []
                for trip in trips:
            time.append([trip[1], trip[0]])
            time.append([trip[2], - trip[0]])
                    time.sort()
        total_passengers_at_a_time = 0
                for ele in time:
            total_passengers_at_a_time+=ele[1]
            if total_passengers_at_a_time > capacity:
                return False
                    return True
        