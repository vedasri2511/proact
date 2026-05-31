class Solution:
    def distributeCandies(self, candyType):
        unique_types = len(set(candyType))
        candies_allowed = len(candyType) // 2

        return min(unique_types, candies_allowed)