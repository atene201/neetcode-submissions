class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Create an empty set
        # Iterate over the array and add each num into the set
        # if the num already exists in the set then it is a duplicate

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        