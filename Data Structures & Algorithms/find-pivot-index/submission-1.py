class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0 # constraint is if where at the left most side: left = 0

        for idx in range(len(nums)):
            right = total - nums[idx] - left
            if right == left:
                return idx
            left += nums[idx]
        return -1