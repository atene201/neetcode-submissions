class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_side = 0

        for i in range(len(nums)):
            right_side = total - nums[i] - left_side
            if left_side == right_side:
                return i
            left_side += nums[i]
        return -1