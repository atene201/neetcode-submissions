class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # is the starting point the lowest value in the list?
        # range from 0 to missing value or largest value + 1

        seen = [False]*len(nums)

        for num in nums:
            if num > 0 and num <= len(nums):
                seen[num-1] = True
        
        for i in range(1, len(nums)+1):
            if seen[i-1] == False:
                return i
        return len(nums) + 1

        