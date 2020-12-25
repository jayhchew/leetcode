class Solution:
    """
    Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

    For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them.

    Notice that multiple kids can have the greatest number of candies.
    """
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        alt = candies.copy()
        alt.sort()
        largest = alt[len(alt) - 1]
        lis = []
        for i in candies:
            if (i + extraCandies) >= largest:
                lis.append(True)
            else:
                lis.append(False)
        return lis
