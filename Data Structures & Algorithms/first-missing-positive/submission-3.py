class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # is the starting point the lowest value in the list?
        # range from 0 to missing value or largest value + 1

        nums.sort()
        missing_pos = 1

        for num in nums:
            if num > 0 and num == missing_pos:
                missing_pos += 1
        return missing_pos

        