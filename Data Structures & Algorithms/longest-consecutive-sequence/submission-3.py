class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        max_sequence = 0

        for num in nums:
            if (num - 1) not in seen: # it is the start of a sequence
                length = 0
                while (num + length) in seen:
                    length += 1
                if length > max_sequence:
                    max_sequence = length
        return max_sequence

